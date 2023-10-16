import cv2 as cv

img = cv.imread('fabio-unsplash.jpg')
newimg = cv.resize(img, (900, 500), fx=1, fy=0.5, interpolation=cv.INTER_CUBIC)

cv.imshow('window', newimg)
cv.imwrite('fabio-resize.jpg', newimg)
cv.waitKey(0)
cv.destroyAllWindows()
