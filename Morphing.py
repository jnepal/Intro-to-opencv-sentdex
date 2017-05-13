import numpy
import cv2

#capturing video feed
capture = cv2.VideoCapture(0)#captures the video feed of 1st webcam

while True:
    ret, frame = capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #HSV Hue saturation color
    lowerValue  = numpy.array([100, 150, 35])#hit and trial value
    upperValue  = numpy.array([180, 255, 150]) #hit an trial values

    mask   = cv2.inRange(hsv, lowerValue, upperValue)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    '''Morphological Transformation '''
    kernel   = numpy.ones((5, 5), numpy.uint8)
    #Erosion : it scans the area and if all the pixels around are of identical color it moves on
    #but if any pixel inside slide is other than of other pixels say 1 pixel is white among many black pixels
    #it removes the white pixel
    erosion  = cv2.erode(mask, kernel, iterations=1)
    #Dilation does the opposite, it pushesout that pixel of different color to the fullest
    dilation = cv2.dilate(mask, kernel, iterations=1)

    #opening removes false positives noise from background
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN, kernel)

    #closing removes false negatives noise from foreground
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


    ''' There are two more morphology
        tophap   : difference between input media and opening of media
        blackhat : difference between the closing of the input media and input media
     '''
    #media show
    cv2.imshow('Orignal Feed', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)
    cv2.imshow('Erosion', erosion)
    cv2.imshow('Dilation', dilation)
    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)

    #listen the pressed key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#releases the capture
capture.release()
cv2.destroyAllWindows()