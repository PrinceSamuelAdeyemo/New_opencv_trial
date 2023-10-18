import cv2 as cv
import numpy as np


pts = [(25, 25), (150, 25), (75, 150)]
red = (0, 0, 255)

img = np.zeros((1000, 1000, 3), np.uint8)
cv.polylines(img, np.array([pts]), True, red, 1)
cv.imshow('triangle', img)

cv.waitKey(0)
cv.destroyAllWindows()
