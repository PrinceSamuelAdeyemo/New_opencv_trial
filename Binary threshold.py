import numpy as np
import cv2 as cv


def trackbar(x):
    rect, img1 = cv.threshold(img, x, 255, cv.THRESH_BINARY)
    rect, img2 = cv.threshold(img, x, 255, cv.THRESH_BINARY_INV)
    output = np.hstack([img, img1, img2])
    cv.imshow('window', output)


img = cv.imread('sam_pic.jpg')
img = cv.resize(img, (400, 400), None, 0.5, 0.5, interpolation=cv.INTER_CUBIC)
trackbar(100)
cv.createTrackbar('Threshold', 'window', 100, 255, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()
