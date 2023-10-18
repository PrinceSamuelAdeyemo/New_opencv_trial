import cv2 as cv
import numpy as np


pt1, pt2 = (10, 10), (50, 50)
red = (0, 0, 255)
blue = (255, 0, 0)


def mouse(event, x, y, flags, param):
    global pt1, pt2

    if event == cv.EVENT_LBUTTONDOWN:
        pt1 = x, y
        pt2 = x, y

    elif event == cv.EVENT_MOUSEMOVE and flags == 1:
        pt2 = x, y
        img[:] = img0
        cv.rectangle(img, pt1, pt2, red, 1)

    elif event == cv.EVENT_LBUTTONUP:
        pt2 = x, y
        img[:] = img0
        cv.rectangle(img, pt1, pt2, blue, cv.FILLED)
        img0[:] = img

    cv.imshow('multiple lines', img)


img0 = np.zeros((1000, 1000, 3), np.uint8)
img = img0.copy()
cv.imshow('multiple lines', img)
cv.setMouseCallback('multiple lines', mouse)

cv.waitKey(0)
cv.destroyAllWindows()
