import cv2
import numpy

#media read
mainImage = cv2.imread('media/mainImage.jpg')
template  = cv2.imread('media/template.jpg', cv2.IMREAD_GRAYSCALE)

#Color Conversion of media to gray
grayscaleMainImage = cv2.cvtColor(mainImage, cv2.COLOR_BGR2GRAY)

#width and height of the template media
w, h = template.shape[::-1] #template.shape gives height and width whereas template.shape[::-1] gives width and height

''' Matching template '''
result    = cv2.matchTemplate(grayscaleMainImage, template, cv2.TM_CCOEFF_NORMED )
threshold = 0.8 #i.e 80%
location  = numpy.where(result >= threshold)

#Marking on the MainImage
for point in zip(*location[::-1]):
    cv2.rectangle(mainImage, point, (point[0] + w, point[1] + h), (0, 255, 255), 2)
    print(point)
#media show
# cv2.imshow('Template Image', template)
# cv2.imshow('Main Image', mainImage)
cv2.imshow('Match detected', mainImage)

#listen for a pressed key
''' If this is not performed imshow just blinks and fades away '''
cv2.waitKey(0)
cv2.destroyAllWindows()