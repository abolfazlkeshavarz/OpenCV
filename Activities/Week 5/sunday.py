# today we'll learn how callback a mouse action:
# note that this example just draw a circle when you press right button on mouse:

import cv2
import numpy as np

radius = int(input("please enter radius value:\n"))
img = np.zeros((512, 512, 3), dtype=np.uint8)

def draw_circle(self, x, y, flags, param):
    if self == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), radius=radius, color=(0,255,255), thickness= -1)
cv2.namedWindow('Circle Draw:')
cv2.setMouseCallback('Circle Draw:', draw_circle)
while True:
    cv2.imshow('Circle Draw:', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyWindow("Circle Draw:")




img2 = np.zeros((512,512,3), np.uint8)
drawing = False
def Brush(self, x, y, flags, param):
    global drawing
    if self == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif self == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img2, (x,y), radius, (0,255,0), -1)
    else :
        drawing = False
cv2.namedWindow("Brush:")
cv2.setMouseCallback("Brush:", Brush)
while True:
    cv2.imshow('Brush:', img2)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyWindow('Brush:')




defImg = np.zeros((512, 512, 3), np.uint8)
isDraw = False
Color = (255, 255, 255) # we set color to white by default
def customBrush(self, x, y, flags, param):
    global isDraw, Color

    if self == cv2.EVENT_LBUTTONDOWN:
        isDraw = True
    elif self == cv2.EVENT_MOUSEMOVE:
        if isDraw == True:
            cv2.circle(defImg, (x,y), radius, Color, -1)
    else :
        isDraw = False
cv2.namedWindow('customBrush:')
cv2.setMouseCallback('customBrush:', customBrush)
while True:
    
    cv2.imshow('customBrush:', defImg)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('b'):
        Color = (255, 0, 0)
    elif key == ord('g'):
        Color = (0, 255, 0)
    elif key == ord('r'):
        Color = (0, 0, 255)
    elif key == ord('e'):
        Color = (0, 0, 0)
    elif key == ord('w'):
        Color = (255, 255, 255)
    elif key == 32: # this line mean when space button pressed, blank the current Window:
        cv2.rectangle(defImg, (0, 0), (512, 512), (0, 0, 0), -1)
    elif key == 27:
        print('!!! Application Stopped !!!')
        break
cv2.destroyWindow('customBrush:')
