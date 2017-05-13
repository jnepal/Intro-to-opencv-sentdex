import cv2
import numpy

#Capturing video feed from webcam

capture = cv2.VideoCapture(0) #captures the feed from first webcam
i = 0
while True:
    ret, frame = capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #HSV HUE saturation value
    lowerValue  = numpy.array([100, 150, 35])#hit and trial value
    upperValue  = numpy.array([180, 255, 150]) #hit an trial values

    mask    = cv2.inRange(hsv, lowerValue, upperValue) #binary operation value 1 if it is in range otherwise 0
    result  = cv2.bitwise_and(frame, frame, mask=mask)

    ''' Smoothing of Image '''
    kernel = numpy.ones((15, 15), numpy.float32)/15*15
    smoothed = cv2.filter2D(result, -1, kernel)

    gaussianBlur = cv2.GaussianBlur(result, (15, 15), 0)

    medianBlur = cv2.medianBlur(result, 15)

    bilateralFilter = cv2.bilateralFilter(result, 15, 75, 75)


    #Image Show
    cv2.imshow('Frame',frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)
    cv2.imshow('Smoothed', smoothed)
    cv2.imshow('Gaussian Blur', gaussianBlur)
    cv2.imshow('Median Blur', medianBlur)
    cv2.imshow('Median Blur', medianBlur)
    cv2.imshow('Bilateral Filter', bilateralFilter)


    #listens for the pressed key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()