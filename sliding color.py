import cv2 as cv
import numpy as np


def trackbar_change(x):
    img[:, :,2] = 2
    cv.imshow('window', img)

img = np.zeros((1000, 1000, 3), np.uint8)

for i in range(1000):
    img[i, :, 0] = i
    img[:, i, 1] = i

cv.imshow('window', img)
cv.createTrackbar('Scale', 'window', 10, 999, trackbar_change)

cv.waitKey(0)
cv.destroyAllWindows()
