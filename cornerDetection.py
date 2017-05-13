import cv2
import numpy

#media read
image = cv2.imread('media/corner-detection.jpg')
#convert to grayscale
grayscaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

grayscaleImage = numpy.float32(grayscaleImage) #to satisy the algorithm used to find the corner

'''Corner Detection'''
corners = cv2.goodFeaturesToTrack(grayscaleImage, 200, 0.01, 10)
corners = numpy.int0(corners)


for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (x,y), 3, 255, -1)

#media show
cv2.imshow('Corner Detected Image', image)

#listen for pressed key
cv2.waitKey(0)
#destroy all windows
cv2.destroyAllWindows()