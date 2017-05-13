import cv2
import numpy

#Video Feed Capture
capture = cv2.VideoCapture(0) #captuers the video feed from the first webcam

while True:
    ret, frame = capture.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F) #Cv_64F is default datatype(ddepth)
    sobelX    = cv2.Sobel(frame, cv2.CV_64F, 1, 0 , ksize=5) #ksize is kernel size
    sobelY    = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    ''' Edge Detector '''
    cannyEdges =  cv2.Canny(frame, 60, 60)

    #media show
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Laplacian Frame', laplacian)
    cv2.imshow('Sobel X frame', sobelX)
    cv2.imshow('Sobel Y frame', sobelY)
    cv2.imshow('Canny Edge', cannyEdges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release capture
capture.release()
#delete all windows
cv2.destroyAllWindows()