import numpy as np
import cv2
import imutils
'''
This Zoom Program was written by: Carlos J. Flores of F.I.U.
'''
cap = cv2.VideoCapture(0)
ret, frame = cap.read() # Initializing the video frame
# setting width & height of the video frame
width = frame.shape[1] 
height = frame.shape[0]

def Zoom(cv2Object, zoomSize):
    cv2Object = imutils.resize(cv2Object, width=(zoomSize * cv2Object.shape[1]))
    center = (cv2Object.shape[0]//2,cv2Object.shape[1]//2)
    cropScale = (center[0]//zoomSize, center[1]//zoomSize)
    cv2Object = cv2Object[(cropScale[0]) : (center[0] + cropScale[0]), (cropScale[1]) : (center[1] + cropScale[1])]
    return cv2Object

#Zoom(frame, 4)
i = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    print (i)
    # Zooming in
    #frame = imutils.resize(frame, width=1280) #doubling the width
    #frame = frame[240:720,320:960]
    if i > 0:
        frame = Zoom(frame, i)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('a'):
        i +=  1
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        i -= 1
# Releasing the capture
cv2.imwrite("CanvasTest12.png", frame)
cap.release()
cv2.destroyAllWindows()