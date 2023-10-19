import numpy as np
import cv2 as cv


img = cv.imread('sam_pic.jpg')
img = cv.resize(img, None, fx=0.3, fy=0.3, interpolation=cv.INTER_CUBIC)
# M = np.ones(img.shape, dtype= np.uint8) * 40

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
all = np.hstack([img, hsv, lab])

cv.imshow('window', all)

cv.waitKey(0)
cv.destroyAllWindows()
