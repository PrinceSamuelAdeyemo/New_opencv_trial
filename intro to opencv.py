import cv2 as cv

img = cv.imread('sam_pic.png')
cv.imshow('window', img)
cv.displayOverlay('window', 'OVERLAY', delayms=0)
# cv.imwrite('sam_pic.jpg', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite('sam_pic_gray.jpg', gray)
cv.waitKey(0)
cv.destroyAllWindows()
