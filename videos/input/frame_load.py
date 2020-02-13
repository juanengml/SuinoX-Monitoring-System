import numpy as np
import cv2

cap = cv2.VideoCapture("porcos2.mp4")
x = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    x = x  +1 
    print("frames_2/porcos2_%s.jpg" % x)
    cv2.imwrite("frames_2/porcos2_%s.jpg" % x,frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

