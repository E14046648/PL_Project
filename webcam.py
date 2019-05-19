import cv2
import numpy as np
import time

cam = cv2.VideoCapture("http://admin:admin@192.168.0.110:8081")
time.sleep(2)

while True:
    print("123")
    ret,frame = cam.read()
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
