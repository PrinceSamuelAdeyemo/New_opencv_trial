import cv2 as cv
import numpy as np


pt1, pt2 = (10, 10), (50, 50)
red = (0, 0, 255)


def onmouse(event, x, y, flags, param):
    global pt1, pt2

    if event == cv.EVENT_LBUTTONDOWN:
        pt1 = x, y
        pt2 = x, y

    elif event == cv.EVENT_MOUSEMOVE and flags == 1:
        pt2 = x, y

    elif event == cv.EVENT_LBUTTONUP:
        pt2 = x, y

    # xa, ya = str(x), str(y)
    img[:] = 0
    cv.line(img, pt1, pt2, red, 10)
    cv.imshow('Create line', img)
    # cv.putText(img, f"Position: {xa}, {ya}", (5, 5), 1, red, 1)


# cv.namedWindow("Create line")
img = np.zeros((250, 250, 3), np.uint8)
# cv.line(img, pt1, pt2, red)
cv.imshow("Create line", img)
cv.setMouseCallback("Create line", onmouse)
cv.waitKey(0)
cv.destroyAllWindows()
