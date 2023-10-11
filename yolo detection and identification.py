# YOLO Detection
import numpy as np
import cv2 as cv
import time


# Load the image first
img = cv.imread('sam_pic.jpg')
cv.imshow('window', img)
cv.waitKey(0)

# Get the names of  classes and also get random colors
classes = open('coco.names').read().strip().split('\n')
np.random.seed()
colors = np.random.randint(0, 255, size=(len(classes), 3), dtype= np.uint8)

# Give the config and the weights files and load the network
net = cv.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)

# Determine the output layer
ln = net.getLayerNames()
ln = [ln[1[0] - 1] for i in net.getUnconnectedOutLayers()]
print(ln)

# Construct a blob from the image and output it
blob = cv.dnn.blobFromImage(img, 1/255.0, (400, 400), swapRB=True, crop=False)
r = blob[0, 0, :, :]

cv.imshow('blob', r)
cv.waitKey(1)

# load the input into the network
net.setInput(blob)
t0 = time.time()
outputs = net.forward(ln)
t1 = time.time()
print(f'Time: {t1 - t0}')

for out in outputs:
    print(out.shape)


r0 = blob[0, 0, :, :]
r = r0.copy()
cv.imshow('blob', r)
# cv.createTrackbar('confidence', 'blob', 50, 101, trackbar2)


