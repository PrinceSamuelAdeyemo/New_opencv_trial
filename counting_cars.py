import numpy as np
import cv2 as cv
import imutils


# Start the livestream

vid = cv.VideoCapture(0)
vid.set(1, 500)
vid.set(2, 100)
previous_frame = None

while vid.isOpened():
    pressedKey = cv.waitKey(1) & 0xFF
    rect, frame = vid.read()

    frame = cv.flip(frame, 1)
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurgray_frame = cv.GaussianBlur(gray_frame, (21, 21), 0.5)

    # Get the difference between the frames
    #  and save as threshold before doing any other thing
    if previous_frame is None:
        previous_frame = blurgray_frame
        continue
    compare_frame = cv.absdiff(previous_frame, blurgray_frame)
    blurgray_frame = previous_frame
    ret, thresh = cv.threshold(compare_frame, 150, 255, cv.THRESH_BINARY)

    dilate_image = cv.dilate(thresh, None, iterations=2)
    find_contour = cv.findContours(dilate_image.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #contours = cv.drawContours(dilate_image, find_contour, -1, (0, 255, 0), 2)
    contours = imutils.grab_contours(find_contour)
    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        cv.rectangle(contour, (x, y), (x+w, y+h), (0, 255, 0), 2)



    cv.imshow('window', frame)

    if pressedKey == ord('q'):
        break

vid.release()
cv.destroyAllWindows()
