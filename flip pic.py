# import numpy as np
import cv2 as cv


img = cv.imread('sam_pic.jpg')
cv.imshow('window', img)

while True:
    k = cv.waitKey(0)
    if k == ord('q'):
        break
    elif k == ord('v'):
        img = cv.flip(img, 0)
    elif k == ord('h'):
        img = cv.flip(img, 1)

    cv.imshow('window', img)

cv.destroyAllWindows()
