import cv2 as cv


red = (0, 0, 255)
img = cv.imread('zoom meeting.jpg')
cv.imshow('window', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('window 2', gray)

path = 'haarcascade_frontalface_default.xml'
face_detector = cv.CascadeClassifier(path)
rects = face_detector.detectMultiScale(gray,
                                       scaleFactor=1.1,
                                       minNeighbors=10,
                                       flags=cv.CASCADE_SCALE_IMAGE,
                                       minSize=(30, 30))

for rect in rects:
    cv.rectangle(img, rect, red, 2)

cv.imshow('window', img)
cv.waitKey(0)
