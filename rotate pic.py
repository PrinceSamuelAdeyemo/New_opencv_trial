import numpy as np
import cv2 as cv


def rotate(angle):
    # img = cv.imread('sam_pic.jpg')
    M = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv.warpAffine(img, M, (w, h))
    cv.imshow('window', rotated)


img = cv.imread('sam_pic.jpg')
h, w = img.shape[:2]
center = w//2, h//2
cv.imshow('window', img)
cv.createTrackbar('Scale', 'window', 0, 360, rotate)

cv.waitKey(0)
cv.destroyAllWindows()
