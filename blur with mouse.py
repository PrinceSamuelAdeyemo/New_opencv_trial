import cv2 as cv


p0 = 10
p1 = 20


def mouseblur(event, x, y, flags, param):
    global p0, p1

    if event == cv.EVENT_LBUTTONDOWN:
        p0 = x
        p1 = y

    elif event == cv.EVENT_MOUSEMOVE and flags == 1:
        p1 = y
        img2[:] = img
        blurred = cv.blur(img, (p0, p1))
        img2[:] = blurred
        img[:] = img2
        # cv.putText(img, f'{p0} and {p1}', (p0, p1), cv.FONT_ITALIC, 2, (0, 0, 255), 2)
        # img[:] = img2
        # img2[:] = img

    elif event == cv.EVENT_LBUTTONUP:
        p1 = y
        img2[:] = img
        blurred = cv.blur(img, (p0, p1))
        img2[:] = blurred
        # cv.putText(img, f'{p0} and {p1}', (p0, p1), cv.FONT_ITALIC, 2, (0, 0, 255), 2)
        img[:] = img2
        # img2[:] = img

        # img[:] == img2

    cv.imshow('window', img)

img = cv.imread('sam_pic.jpg')
img2 = img.copy()
# img2 = img[:]

cv.imshow('window', img)
cv.setMouseCallback('window', mouseblur)

cv.waitKey(0)
cv.destroyAllWindows()
