from scripts.label_image import label_img
import numpy as np
import cv2, os, shutil, imutils
from datetime import datetime
import tkinter as tk
from tkinter import messagebox



# ----------
# | SET UP |
# ----------

# for camera
cap = cv2.VideoCapture(1)
#cap.set(3, 1920)
#cap.set(4, 1080)
cap.set(5, 60)

# for display
cv2.namedWindow('SmartScope', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('SmartScope', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
font = cv2.FONT_HERSHEY_SIMPLEX
colour = (255, 64, 16) #BGR

# for tkinter
root = tk.Tk()
root.withdraw()

# paths
img_path = 'tf_files/img.jpg'
last_path = 'tf_files/last.jpg'
save_path = 'history/'

# other
detected = None
msg = None
confidence = 0
saved = True
esc = 27
zoomed = False
help_msg = open('tf_files/help_msg.txt', 'r').read()
abspath = os.path.abspath

# make date format file friendly
def str_date():
    return str(datetime.now()).replace(' ', '_').replace('.', '_').replace(':', '-')

# print messages on screen
def print_results(string = None):
    if string == None:
        string = detected + ' detected - confidence: ' + str('%.2f' % (confidence * 100)) + '%'
    cv2.putText(frame, string, (25, 420), font, 0.75, colour, 1, cv2.LINE_AA)

# save last scanned image
def write_img():
    print_results()
    cv2.imwrite(last_path, frame)

# zoom function from github.com/CJoseFlores/python-OpenCV-Zoom/blob/master/ZoomTest.py
def zoom(cv2Object, zoomSize = 2):
    cv2Object = imutils.resize(cv2Object, width = (zoomSize * cv2Object.shape[1]))
    center = (cv2Object.shape[0] // 2, cv2Object.shape[1] // 2)
    cropScale = (center[0] // zoomSize, center[1] // zoomSize)
    cv2Object = cv2Object[cropScale[0] : (center[0] + cropScale[0]), cropScale[1] : center[1] + cropScale[1]]
    return cv2Object



# -------------
# | MAIN LOOP |
# -------------

messagebox.showinfo('Help', help_msg)

while (True):
    # capture frame-by-frame
    ret, frame = cap.read()
    
    # processing user input
    key = cv2.waitKey(1) & 0xFF
    if key == esc:
        break
    elif key == ord(' '):
        cv2.imwrite(img_path, frame)
        detected, confidence = label_img()
        write_img()
        saved = False
    elif key == ord('s'):
        if saved == False:
            saved = True
            shutil.move(abspath(last_path), abspath(save_path + detected + '_' + str_date() + '.jpg'))
            msg = 'Image saved'
        else:
            msg = 'Image does not exist or already saved'
    elif key == ord('/') or key == ord('?'):
         messagebox.showinfo('Help', help_msg)
    elif key == ord('c'):
        detected = None
        msg = None
    elif key == ord('z'):
        zoomed = not zoomed
    
    # show text on frame
    if zoomed:
        frame = zoom(frame)

    cv2.putText(frame, 'SmartScope', (0, 25), font, 1, colour, 3, cv2.LINE_AA)

    if (detected != None):
        print_results()
    elif msg != None:
        print_results(msg)

    cv2.imshow('SmartScope', frame)



# -----------------
# | EXIT ROUTINES |
# -----------------

# remove unnecessary files
try:
    os.remove(img_path)
    os.remove(last_path)
except:
    # if the file does not exist
    pass
    # what did you expect!? printing two thousand error messages and halting the computer just because a file that should be deleted does not exist?

# when everything done, release the capture
cap.release()
cv2.destroyAllWindows()
