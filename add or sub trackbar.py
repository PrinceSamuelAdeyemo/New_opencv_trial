import numpy as np
import cv2 as cv


def light_it(value):
    img = cv.imread('sam_pic.jpg')
    img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
    M = np.ones(img.shape, dtype = np.uint8) * value
    bright = cv.add(img, M)
    both = np.hstack([img, bright])
    cv.imshow('window', both)


img = cv.imread('sam_pic.jpg')
img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
cv.imshow('window', img)
cv.createTrackbar('Lightness', 'window', 0, 100, light_it)

cv.waitKey(0)
cv.destroyAllWindows()
