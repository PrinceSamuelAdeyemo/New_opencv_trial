import numpy as np
import cv2 as cv


path = 'haarcascade_frontalface_default.xml'
face_detector = cv.CascadeClassifier(path)
red = (0, 0, 255)


def detect():

    face_rects = face_detector.detectMultiScale(gray_vid,
                                   scaleFactor=1.1,
                                   minNeighbors=3,
                                   flags=cv.CASCADE_SCALE_IMAGE,
                                   minSize=(30, 30))
    for rectan in face_rects:
        cv.rectangle(gray_vid, rectan, red, 2)


cap = cv.VideoCapture(0)

while True:
    rect, frame = cap.read()
    gray_vid = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    detect()

    cv.imshow('window', gray_vid)

    if cv.waitKey(1) and 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
