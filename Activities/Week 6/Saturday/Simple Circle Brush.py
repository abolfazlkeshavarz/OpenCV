import cv2
import numpy as np
import matplotlib.pyplot as plt

zeros = np.zeros((512, 512, 3), np.uint8)
radius = 10
draw = False
Color = (255, 255, 255)
def brush(self, x, y, flags, param):
    global draw
    if self == cv2.EVENT_LBUTTONDOWN:
        draw = True
    elif self == cv2.EVENT_MOUSEMOVE:
        if draw == True:
            cv2.circle(zeros, (x,y), radius, Color, -1)
    elif self == cv2.EVENT_LBUTTONUP:
        draw =False

cv2.namedWindow('Paint')
cv2.setMouseCallback('Paint', brush)

while True:
    cv2.imshow('Paint', zeros)
    key = cv2.waitKey(1) & 0XFF
    if key == ord('b'):
        Color = (255, 0, 0)
    elif key == ord('g'):
        Color = (0, 255, 0)
    elif key == ord('r'):
        Color = (0, 0, 255)
    elif key == ord('e'):
        Color = (0, 0, 0)
    elif key == 32:
        zeros = np.zeros((512, 512, 3), np.uint8)
    elif key == 27 :
        break
cv2.destroyAllWindows()