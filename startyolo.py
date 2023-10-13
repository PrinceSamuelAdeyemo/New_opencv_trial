import numpy as np
import cv2 as cv


img = cv.imread('sam_pic.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

net = cv.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)

layer_names = net.getLayerNames()
unconnected_layer_names = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]
print(unconnected_layer_names)

img_blob = cv.dnn.blobFromImage(img, 1/255, (500, 500), swapRB=True, crop=False)
net.setInput(img_blob)
net.forward(layer_names)
# face_detect = cv.FaceDete
