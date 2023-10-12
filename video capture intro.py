import cv2 as cv

videocap = cv.VideoCapture(0)
while True:
    rec, frame = videocap.read()

    grayvideo = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('My gray Video', frame)
#    cv.imwrite('grayvideo.avi', frame, params = None)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

videocap.release()
cv.destroyAllWindows()
