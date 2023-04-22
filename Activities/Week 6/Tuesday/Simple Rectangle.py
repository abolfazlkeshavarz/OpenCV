import cv2
import numpy as np
from matplotlib import pyplot as plt

zeros = np.zeros((512, 512, 3), dtype = np.uint8)
Color = (255, 0, 0)
drawing = False
start = (0, 0)

def rectangle(event, x1, y1, flags, param):
    global drawing, start
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start = x1,y1
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True :
            start = x1, y1
            cv2.rectangle(zeros,start, (x1, y1), Color, 3 )
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.namedWindow('Rectangle')
cv2.setMouseCallback('Rectangle', rectangle)

while True:
    cv2.imshow('Rectangle', zeros)
    key = cv2.waitKey(1) & 0XFF
    if key == 27:
        break
    elif key == ord('b'):
        Color = (255, 0, 0)
    elif key == ord('g'):
        Color = (0, 255, 0)
    elif key == ord('r'):
        Color = (0, 0, 255)
    elif key == 32:
        zeros = np.zeros((512, 512, 3), 'uint8')

cv2.destroyAllWindows()