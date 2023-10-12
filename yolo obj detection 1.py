import numpy as np
import cv2 as cv
import time

# deal with the images first
img = cv.imread('sam_pic.jpg')
cv.imshow('window', img)
cv.waitKey(1)

# Bring in the config and the weight files first and then load the network.
net = cv.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)

# Get layer names
ln = net.getLayerNames()
print(len(ln), ln)

# Now create a blob
blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)
r = blob[0, 0, :, :]

# Show the blob for like a milliseconds
cv.imshow('blob', r)
cv.waitKey(1)

# Set the blob object as an input to the network
net.setInput(blob)
t0 = time.time()
outputs = net.forward(ln)
t1 = time.time()
print(t1-t0)

# Now output the total result with the original image
cv.imshow('window', img)
print(t1-t0)
cv.waitKey(0)

cv.destroyAllWindows()
