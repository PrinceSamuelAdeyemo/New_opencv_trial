from matplotlib import pyplot as plt
import cv2 as cv


img = cv.imread('sam_pic.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
calcHist = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title('Gray histogram')
plt.xlabel('Color')
plt.ylabel('# of pixel')
plt.plot(calcHist)
plt.xlim([00, 256])
plt.ylim([0, 2000])
plt.show()

cv.waitKey(0)
