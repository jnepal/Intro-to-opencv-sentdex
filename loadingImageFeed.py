import cv2
import numpy as np
import matplotlib.pyplot as plot

'''
Opencv treats media as BGRA instead of RGBA; A alpha value
Other options are IMREAD_COLOR = 1 and IMREAD_UNCHANGED = -1 , IMAGE_GRAYSCALE = 0
(also 0 can be provided instead of IMREAD_GRAYSCALE )

'''

image = cv2.imread('media/watch.jpg', cv2.IMREAD_GRAYSCALE)

'''Imshow shows the media'''
cv2.imshow('media', image) # 'media' is the title bar name
cv2.waitKey(0) #Waits for any key to be pressed 0 doesn't work for video
cv2.destroyAllWindows() #destroys the windows

# plot.imshow(media, cmap='gray', interpolation='bicubic')
# plot.plot([50,100], [80,100], 'c', linewidth = 5)# c represents color
# plot.show()

#saving the media
#cv2.imwrite('watchgray.png', media)