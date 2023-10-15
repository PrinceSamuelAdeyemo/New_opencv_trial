import cv2 as cv
import numpy as np

pts = [(25, 25), (150, 25), (70, 150)]
red, blue = (0, 0, 255), (255, 0, 0)
def mouse_click(event, x, y, z, flagsm):
    global pts

    if event == cv.EVENT_LBUTTONDOWN:
        pts = x, y, z

    elif event == cv.EVENT_MOUSEMOVE and flags == 1:
        pts = x, y, z
        img[:] = img0
        cv.polylines(img, np.array([pts]), True, red, 1)

    elif event == cv.EVENT_LBUTTONUP:
        pts = x, y, z
        img[:] = img0
        cv.polylines(img, np.array([pts]), True, blue, 2)
        img0[:] = img

    cv.imshow('multiple polygons', img)

img0 = np.zeros((1000, 1000, 3), np.uint8)
img = img0.copy()
# cv.polylines(img, np.array([pts]), True, red, 1)
cv.imshow('multiple polygons', img)
cv.setMouseCallback("multiple polygons", mouse_click)

cv.waitKey(0)
cv.destroyAllWindows()
