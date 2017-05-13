import cv2
import numpy

#Image Load
image1 = cv2.imread('media/3D-Matplotlib.png')
image2 = cv2.imread('media/python.jpg')


# print(image1.shape)#gives the rows, cols and channels of the media

rows, cols, channels = image1.shape
roi = image1[0: rows, 0: cols]

#Converting the image2 to Grayscale (Masking)
image2gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

#threshold
'''
    #color Inversion

    If the pixel value is greater than 220, it will be converted to 255 i.e white
    If the pixel value is less than 220, it will be converted to black
    Binary threshold so value will be either 1 or 0
    Binary_Inv is going to inverse those values like color inversion
'''
ret, mask = cv2.threshold(image2gray, 220, 255, cv2.THRESH_BINARY_INV)

#Returns the black area of the media i.e area not masked
#Color Inversion of mask
maskInv = cv2.bitwise_not(mask)

#Background and Foreground of media
image1Bg = cv2.bitwise_and(roi, roi, maskInv)
image2Fg = cv2.bitwise_and(image2, image2, mask)


# dst = cv2.add(image1Bg , image2Fg) #for adding operation both images should be of same size
# image1[0:rows, 0:cols] = dst

#Image Show

cv2.imshow('Mask', mask)
cv2.imshow('Orignal Image', image2)
cv2.imshow('Mask Inverse', maskInv)
cv2.imshow('Image 1 Original ', image1)
cv2.imshow('Image 1 Background colour', image1Bg)
cv2.imshow('Image 2 Foreground colour', image2Fg)
# cv2.imshow('dst', dst)


#listen for key pressed
cv2.waitKey(0)
cv2.destroyAllWindows() #destroy all windows after any key is pressed