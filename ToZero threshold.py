import numpy as np
import cv2 as cv


def trackbar(x):
    rect, img1 = cv.threshold(img, x, 255, cv.THRESH_BINARY)
    rect, img2 = cv.threshold(img, x, 255, cv.THRESH_BINARY_INV)
    rect, img3 = cv.threshold(img, x, 255, cv.THRESH_TOZERO)
    rect, img4 = cv.threshold(img, x, 255, cv.THRESH_TOZERO_INV)
    rect, img5 = cv.threshold(img, x, 255, cv.THRESH_TRUNC)
    # rect, img6 = cv.threshold(img, x, 255, cv.THRESH_TRIANGLE)
    output = np.hstack([img, img1, img2, img3, img4, img5])
    cv.imshow('window', output)


img = cv.imread('sam_pic.jpg')
img = cv.resize(img, (200, 200), None, 0.5, 0.5, interpolation=cv.INTER_CUBIC)
trackbar(0)
cv.createTrackbar('Threshold', 'window', 0, 255, trackbar)


cv.waitKey(0)
cv.destroyAllWindows()
