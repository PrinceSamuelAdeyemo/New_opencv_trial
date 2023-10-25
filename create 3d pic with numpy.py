# import numpy as np
import cv2 as cv
import PyQt5 as pqt

img = cv.imread('sam_pic.jpg')
p0 = 10, 10
p1 = 100, 100
p2 = 250, 250
cv.line(img, p0, p1, (0, 0, 255), 2)
cv.line(img, p1, p2, (0, 255, 0), 5)
cv.imshow('Lines on my pic', img)
# cv.displayOverlay('win', "hek")
cv.createTrackbar()
cv.waitKey(0)
cv.destroyAllWindows()
