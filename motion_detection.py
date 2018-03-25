import cv2
import numpy as np

cap=cv2.VideoCapture('Path to the video file')  #or give live camera feed using 0 or whichever you're using
fgbg=cv2.createBackgroundSubtractorMOG2()

while True:
        _,frame=cap.read()
        fgmask=fgbg.apply(frame)

        cv2.imshow('original',frame)
        cv2.imshow('motion',fgmask)

        k=cv2.waitKey(1) & 0xff
        if k==27:
                break
cap.release()
cv2.destroyAllWindows()

