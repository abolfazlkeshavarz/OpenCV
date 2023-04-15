import cv2
import numpy as np

Zeros = np.zeros((512, 512, 3), np.uint8)
draw = False
ix = 0
iy = 0
Color = (255, 255, 255)
Thikness = int(input('Enter the Thikness:\n'))
def Draw(self, x, y , flags, params):
    global draw, ix, iy
    if self == cv2.EVENT_LBUTTONDOWN:
        draw = True
        ix = x
        iy = y
    elif self == cv2.EVENT_MOUSEMOVE:
        if draw == True:
            cv2.line(Zeros, (ix, iy), (x, y), Color, Thikness)
            ix = x
            iy = y
    elif self == cv2.EVENT_LBUTTONUP:
        draw = False
cv2.namedWindow('Linear Brush')
cv2.setMouseCallback('Linear Brush', Draw)
while True:
    cv2.imshow('Linear Brush', Zeros)
    key = cv2.waitKey(1) & 0XFF
    if key == ord('b'):
        Color = (255, 0, 0)
    elif key == ord('g'):
        Color = (0, 255, 0)
    elif key == ord('r'):
        Color = (0, 0, 255)
    elif key == ord('e'):
        Color = (0, 0, 0)
    elif key == 49:
        Thikness = 1
    elif key == 50:
        Thikness = 2
    elif key == 51:
        Thikness = 3
    elif key == 52:
        Thikness = 4
    elif key == 53:
        Thikness = 5
    elif key == 54:
        Thikness = 6
    elif key == 55:
        Thikness = 7
    elif key == 32 :
        Zeros = np.zeros((512, 512, 3), dtype='uint8')
    elif key == 27 :
        break
cv2.destroyAllWindows()