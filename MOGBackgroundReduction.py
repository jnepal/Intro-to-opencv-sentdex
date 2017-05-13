#works greats in video frame too

import cv2
import numpy as np

#video capture
capture = cv2.VideoCapture('media/people-walking.mp4')
#foreground background
fgBg    =  cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = capture.read()
    fgMask     = fgBg.apply(frame)

    #image show
    cv2.imshow('Orignal Frame', frame)
    cv2.imshow('Foreground Mask', fgMask)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
#release the capture
capture.release()

#destroy the windows
cv2.destroyAllWindows()