import cv2, time
import darknet as dn
import tkinter as tk
from tkinter import messagebox
from collections import deque
from shutil import copyfile
from datetime import datetime
from os.path import abspath


# ----------
# | SET UP |
# ----------

# camera
cap = cv2.VideoCapture(1)
#cap.set(3, 1920)
#cap.set(4, 1080)
cap.set(5, 60)

# display
cv2.namedWindow('SmartScope', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('SmartScope', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
fontface = cv2.FONT_HERSHEY_SIMPLEX
colour = (128, 200, 255) #BGR

# darknet
path = '/path/to/darknet/'
net = dn.load_net(path + 'cfg/yolov3.cfg', path + 'yolov3.weights', 0)
meta = dn.load_meta(path + 'cfg/coco.data')
dn.set_gpu(0)

# tkinter
root = tk.Tk()
root.withdraw()

# other
show_trajectory = True
recording = False
esc = 27
msg = None
q = deque()
save_path = 'saved/macro/'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
with open('macro/help_msg.txt', 'r') as f:
    help_msg = f.read()

def rd (x):
    return int(round(x))

# date in a file name friendly format
def str_date():
    return str(datetime.now()).replace(' ', '_').replace('.', '_').replace(':', '-')

# shows a message on screen
def print_msg(string):
    cv2.putText(frame, string, (25, 420), fontface, 0.75, colour, 1, cv2.LINE_AA)

# -------------
# | MAIN LOOP |
# -------------

while(True):
    # capture frame-by-frame
    ret, frame = cap.read()

    # processing user input
    key = cv2.waitKey(1) & 0xFF
    if key == esc:
        break

    elif key == ord('s'):
        copyfile('macro/img.jpg', abspath(save_path + str_date() + '.jpg'))
        msg = 'Image saved'

    elif key == ord('/') or key == ord('?'):
        messagebox.showinfo('Help', help_msg)

    elif key == ord('t'):
        show_trajectory = not show_trajectory
        if show_trajectory:
            msg = 'Showing trajectory'
        else:
            msg = 'Hiding trajectory'

    elif key == ord('r'):
        if recording:
            out.release()
            msg = 'Saved recording'
        else:
            out = cv2.VideoWriter(save_path + str_date() + '.avi', fourcc, 20, (640,480))
            msg = 'Recording'
        recording = not recording

    elif key == ord('c'):
        msg = None

    cv2.imwrite('macro/img.jpg', frame)

    # computing  output
    results = dn.detect(net, meta, path + 'python/img.jpg')

    # displaying objects
    for ob in results:
        print (ob)
        print ('\n')
        coord = ob[2]
        coord = rd(coord[0]), rd(coord[1]), rd(coord[2]), rd(coord[3])
        cv2.ellipse(frame, (coord[0], coord[1]),(coord[2], coord[3]), 0, 0,
                    360, (0, 255, 0), 3)
        cv2.putText(frame, ob[0], (coord[0], coord[1]), fontface, .75, colour,
                    1, cv2.LINE_AA)
        q.append((coord[0], coord[1]))
        if len(q) > 6000:
            q.popleft()

    # highlighting trajectory
    if show_trajectory:
        for point in q:
            cv2.circle(frame,point, 2, (0,0,255), -1)

    if recording:
        out.write(frame)

    # operations om frame
    if msg != None:
        print_msg(msg)
    cv2.putText(frame,'SmartScope', (0, 25), fontface, 1, colour, 3, cv2.LINE_AA)
    cv2.imshow('SmartScope', frame)
    cv2.imwrite('macro/img.jpg', frame)

    print ('\n')
    time.sleep(0.01)


# -----------------
# | EXIT ROUTINES |
# -----------------

# remove unnecessary files
try:
    os.remove('macro/img.jpg')
except:
    pass

# when everything done, release the capture
if recording:
    out.release()
cap.release()
cv2.destroyAllWindows()
