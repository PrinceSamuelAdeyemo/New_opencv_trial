import numpy as np
import cv2 as cv

img = cv.imread('sam_pic.jpg', cv.IMREAD_GRAYSCALE)
img = cv.resize(img, (600, 400), None, 0.5, 0.5, interpolation=cv.INTER_CUBIC)

cannypic = cv.Canny(img, 100, 200)
both = np.hstack([img, cannypic])

cv.imshow('window', both)

cv.waitKey(0)
cv.destroyAllWindows()
