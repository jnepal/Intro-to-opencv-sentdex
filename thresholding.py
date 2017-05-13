import cv2
import numpy

#media Read
image = cv2.imread('media/bookpage.jpg')
#low light media so threshold is taken low
retval, threshold = cv2.threshold(image, 12, 255, cv2.THRESH_BINARY)

#Converting media to grayscale
grayscaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaleImage, 12, 255, cv2.THRESH_BINARY)

#Adaptive threshold
adaptiveThreshold = cv2.adaptiveThreshold(grayscaleImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

#Otxu Threshold
retval3, otsuThreshold = cv2.threshold(grayscaleImage, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#Image show
cv2.imshow('Image',image)
cv2.imshow('Threshold',threshold)
cv2.imshow('Grayscale Threshold',threshold2)
cv2.imshow('Adaptive Grayscale Threshold',adaptiveThreshold)
cv2.imshow('Otsu Grayscale Threshold',otsuThreshold)

#listens the pressed key
cv2.waitKey(0)

#destroy all the windows
cv2.destroyAllWindows()