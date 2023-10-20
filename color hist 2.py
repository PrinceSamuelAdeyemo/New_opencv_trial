import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('sam_pic.jpg')
colors = 'b', 'g', 'r'
channels = cv.split(img)


plt.figure()
plt.title('Flattened color histogram')
plt.xlabel('Colors')
plt.ylabel('# of pixels')


for (chan, color) in zip(channels, colors):
    hist = cv.calcHist(chan, [0], None, [256], [0, 255])
    plt.plot(hist, color=color)
    plt.xlim = [0, 256]
    plt.ylim = [0, 2000]

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
