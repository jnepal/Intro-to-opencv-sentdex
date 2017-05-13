import cv2
import numpy

#loading cascade
faceCassade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
eyeCassade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')

#capturing Video Feed from webcam
capture = cv2.VideoCapture(0) #gets video feed from first webcame

while True:
    ret, frame = capture.read()
    grayscale  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces      = faceCassade.detectMultiScale(grayscale, 1.3, 5)


    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

        '''For eyes'''
        roiGray  = grayscale[y:y+h, x:x+w] #y then x because plotting is done as y then x
        roiColor = frame[y:y+h, x:x+w]

        eyes = eyeCassade.detectMultiScale(roiGray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roiColor, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        #image show
        cv2.imshow('Image', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

#releases the capture
capture.release()
#destroy All windows
cv2.destroyAllWindows()
