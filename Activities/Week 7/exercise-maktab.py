import cv2
import numpy as np

Zeros = np.zeros((512,512,3), np.uint8)
point1 = [0, 0]
point2 = [0, 0]
color = (255, 255, 255)
def triangle(self, x1, y1, flags, params):
    global point1, point2, color
    if self == cv2.EVENT_LBUTTONDOWN:
        pts = np.array([[x1, y1], [x1-10, y1-10],[x1+10, y1-10]],np.int32)
        pts = pts.reshape((-1, 1, 2))
        isClosed = True
        thickness = 2
        cv2.polylines(Zeros, [pts], isClosed, color, thickness)

cv2.namedWindow('Triangle drawer')
cv2.setMouseCallback('Triangle drawer', triangle)
while True:
    cv2.imshow('Triangle drawer', Zeros)
    key = cv2.waitKey(1) & 0XFF
    if key == 27:
        break
    elif key == ord('b'):
        color = (255, 0, 0)
    elif key == ord('g'):
        color = (0, 255, 0)
    elif key == ord('r'):
        color = (0, 0, 255)
    elif key == 32 :
        Zeros=np.zeros((512, 512, 3), np.uint8)

cv2.destroyAllWindows() 
