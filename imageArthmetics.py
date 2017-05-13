import cv2
import numpy

#media load

image1 = cv2.imread('media/3D-Matplotlib.png')
image2 = cv2.imread('media/mainsvmimage.png')
image3 = cv2.imread('media/python.jpg')

'''Addittion Operation'''

#add = image1 + image2 #retains both solid color/opacity

#Inbuilt version of cv2
add = cv2.add(image1, image2) #adds the each pixel value of both media. so, when the addition is >= 255 it assign 255

#Another method
weighted = cv2.addWeighted(image1, 0.6, image2,0.4 ,0) #0.6 is opacity of first media file

'''Image Show'''
# Orignal Image
# cv2.imshow('Image 1', image1)
# cv2.imshow('Image 2', image2)

cv2.imshow('Image Addittion', add)
cv2.imshow('Weighted', weighted)

#listen for key
cv2.waitKey(0)
cv2.destroyAllWindows()