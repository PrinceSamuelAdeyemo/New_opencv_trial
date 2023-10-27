import numpy as np
import cv2 as cv


img = cv.imread('sam_pic.jpg')
img = cv.resize(img, None, fx=0.3, fy=0.3, interpolation=cv.INTER_CUBIC)
M = np.ones(img.shape, dtype='uint8') * 40

brighter = cv.add(img, M)
darker = cv.subtract(img, M)

img2 = np.hstack([img, brighter, darker])
cv.imshow('window', img2)

cv.waitKey(0)
cv.destroyAllWindows()
