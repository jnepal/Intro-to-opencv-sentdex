import cv2
import numpy

#loading Image
image = cv2.imread('media/watch.jpg', cv2.IMREAD_COLOR);

#Drawing Line
cv2.line(image, (0,0), (150,150), (255, 0, 0) ) #(0,0) is starting point and (150,150) is ending point; (255, 0, 0) is blue color BGR

#Drawing Rectangle

cv2.rectangle(image, (15,25), (200,150), (0, 255, 0), 5)

#Drawing Circle
cv2.circle(image, (100,63), 55, (0, 0, 255) , -1)

#Drawing Polygons
points = numpy.array([[10, 5], [20, 30], [70, 20], [50,10]] , numpy.int32) #numpy array; numpy.int32 is the data type
# points = points.reshape((-1, 1, 2)) #Reshapes the array by 0.5 #optional

cv2.polylines(image, [points], True, (0, 255, 255), 3) #Here providing -1 to line thickness wont fill the polygon

#Drawing Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "Open CV Tutorial", (0, 130), font, 1, (255, 255, 255), 5, cv2.LINE_AA)

#media Show
cv2.imshow('Image', image)

cv2.waitKey(0) #listens the any key pressed
cv2.destroyAllWindows() #destroys all the windows