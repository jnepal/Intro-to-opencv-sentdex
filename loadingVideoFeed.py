import cv2
import numpy

capture = cv2.VideoCapture(0) #0 captures the first video webcam ,any parameter instead of 0 like 'video.flv' loads the video file

#saving the video file

# fourcc = cv2.VideoWriter_fourcc(*'XVID') #codec
# out    = cv2.VideoWriter('output.avi', fourcc, 60.0, (640,480))

while True:
    ret, frame = capture.read() #ret will return boolean value
    gray       = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converting the color of the frame to gray

    #out.write(frame) #saves the frame of the video file

    cv2.imshow('Frame',frame)#'Frame' is just a name of titlebar
    cv2.imshow('Gray Frame', gray)

    #if key pressed == q then break and come out of the loop
    #ord gives the asci value of the key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the camera used
capture.release()
#relasing the video writer output
# out.release()
cv2.destroyAllWindows()