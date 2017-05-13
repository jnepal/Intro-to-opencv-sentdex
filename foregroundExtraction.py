import cv2
import numpy
import matplotlib.pyplot as plot

#media read
image = cv2.imread('media/foregroundExtraction.jpg')


#mask
mask = numpy.zeros(image.shape[:2], numpy.uint8) #numpy.uint8 is datatype

#background Model
backgroundModel = numpy.zeros((1, 65), numpy.float64)

#foreground Model
foregroundModel = numpy.zeros((1, 65), numpy.float64)

rectangle = (50, 50, 300, 500) #this is only variable to be changed for other media too

''' Grab Cut '''
cv2.grabCut(image, mask, rectangle, backgroundModel, foregroundModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = numpy.where((mask == 2) | (mask == 0), 0, 1).astype('uint8') #here 2 and 0 represents foreground where 1 and 3 represents background
image = image*mask2[:,:,numpy.newaxis]

#media show using matplotlib
plot.imshow(image)
plot.colorbar()
plot.show()



