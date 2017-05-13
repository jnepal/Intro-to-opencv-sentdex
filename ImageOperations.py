import numpy
import cv2

#Image Read
image = cv2.imread('media/watch.jpg', cv2.IMREAD_COLOR)

#Refrencing a particular pixel color value
pixel = image[55, 55]

#Changing the color value of pixel
# media[55, 55] = [255, 255, 255]

#Region of Image ROI
roi = image[100:150, 100:150]

#print(roi)

#Changing the color value of Region of Image
image[100:150, 100:150] = [255, 0, 0]


#Copy and Paste ROI
source =  image[37:111 , 107:194]

image[0:74, 0:87] = source

#Showing the Image
cv2.imshow('media', image)


#listens to any key pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
