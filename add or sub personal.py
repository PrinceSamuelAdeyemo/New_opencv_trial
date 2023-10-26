import numpy as np
import cv2 as cv


img = cv.imread('sam_pic.jpg')
img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_LINEAR)
M = np.ones(img.shape, dtype='uint8') * 10

brighter = cv.add(img, M)
pictures = np.hstack([img, brighter])
cv.imshow('window', pictures)
cv.waitKey(0)
cv.destroyAllWindows()
