import cv2 as cv
import numpy as np


pt1, pt2 = (10, 10), (50, 50)
red, blue = (0, 0, 255), (255, 0, 0)

def mouse_click(event, x, y, flags, param):
    global pt1, pt2

    if event == cv.EVENT_LBUTTONDOWN:
        pt1 = x, y
        pt2 = x, y

    elif event == cv.EVENT_MOUSEMOVE and flags == 1:
        pt2 = x, y
        # Give all the properties of img0 to img
        img[:] = img0
        # draw on img
        cv.line(img, pt1, pt2, red, 1)
        # cv.imshow('RETEST', img)

    elif event == cv.EVENT_LBUTTONUP:
        pt2 = x, y
        # Give all the properties of img0 to img
        img[:] = img0
        # draw on img0
        cv.line(img, pt1, pt2, blue, 2)
        # Give all the properties of img back to img0
        img0[:] = img
        # cv.imshow('RETEST', img)

    cv.imshow("RETEST", img)


img0 = np.zeros((1000, 1000, 3), np.uint8)
img = img0.copy()
cv.imshow('RETEST', img)
# cv.line(img, pt1, pt2, blue, 2)

cv.setMouseCallback("RETEST", mouse_click)

cv.waitKey(0)
cv.destroyAllWindows()
