import cv2
import numpy as np
import matplotlib.pyplot as plt

Zeros = np.zeros((1080, 1920, 3), np.uint8)
start_point = (0, 0)
drawing = False
ix = 0
iy = 0
def rectangle_Brush(self, x, y, flags, param):
    global ix, iy, drawing
    if self == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y
    elif self == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(Zeros, (ix, iy), (x, y), (255,0,0),3)
            ix = x
            iy = y
    elif self == cv2.EVENT_LBUTTONUP:
        drawing = False
cv2.namedWindow('Brush')
cv2.setMouseCallback('Brush', rectangle_Brush)
while True:
    cv2.imshow('Brush', Zeros)
    Key = cv2.waitKey(1) & 0XFF
    if Key == 27 :
        cv2.imwrite('FN.jpg', Zeros)
        break
cv2.destroyAllWindows()