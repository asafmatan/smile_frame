import numpy as np
import cv2

import numpy as np
import sys

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')



#cap = cv2.VideoCapture(0)


from picamera.array import PiRGBArray
from picamera import PiCamera
import time

IM_WIDTH = 640
IM_HEIGHT = 480







# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (IM_WIDTH,IM_HEIGHT)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(IM_WIDTH,IM_HEIGHT))
rawCapture.truncate(0)


# allow the camera to warmup
time.sleep(1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
#while 1:
    #ret, img = cap.read()
    img = frame.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    ###Face detection
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        ###smile detection
        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.7,
            minNeighbors=22,
            minSize=(25, 25),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        ##Eye Detection
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            #print (("Found"), len(eyes), ("eyes!"))

        # Set region of interest for smiles
        for (x, y, w, h) in smile:
            print (("Found"), len(smile), ("smiles!"))
            cv2.rectangle(roi_color, (x, y), (x + w, y + h), (0, 0, 255), 1)
            image = cv2.imread('pic.png')
            cv2.namedWindow("Face1", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Face1",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow('Face1', image)
            cv2.waitKey(3000)
            cv2.destroyWindow("Face1")

    cv2.namedWindow("Face", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Face",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Face', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    rawCapture.truncate(0)
#cap.release()
cv2.destroyAllWindows()
