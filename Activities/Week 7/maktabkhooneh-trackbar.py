import cv2
import numpy as np

window_title = 'Brush with Change'
blueTB = 'Blue:'
greenTB = 'Green:'
redTB = 'Red:'
thicknessTB = 'Thickness:'

def BlueTrackbar(val):
    global blue
    blue = val
def GreenTrackbar(val):
    global green
    green = val
def RedTrackbar(val):
    global red
    red = val
def ThiknessTrackbar(val):
    global Thickness
    Thickness = val



Zeros = np.zeros((512, 512, 3), np.uint8)
start_point = (0, 0)
drawing = False
ix = 0
iy = 0
Thickness = 3
blue = 255
green = 255
red = 255
color = (blue, green, red)

def rectangle_Brush(self, x, y, flags, param):
    global ix, iy, drawing, color, Thikness
    if self == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y
    elif self == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(Zeros, (ix, iy), (x, y), color, Thickness)
            ix = x
            iy = y
    elif self == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.namedWindow(window_title)
cv2.setMouseCallback(window_title, rectangle_Brush)
cv2.createTrackbar(blueTB, window_title, 255, 255, BlueTrackbar)
cv2.createTrackbar(greenTB, window_title, 255, 255, GreenTrackbar)
cv2.createTrackbar(redTB, window_title, 255, 255, RedTrackbar)
cv2.createTrackbar(thicknessTB, window_title, 3, 20, ThiknessTrackbar)

while True:
    cv2.imshow(window_title, Zeros)
    Key = cv2.waitKey(1) & 0XFF
    if Key == 27 :
        break
    elif Key == 32: #you can blank the screen by enter space!
        Zeros = np.zeros((512, 512, 3), np.uint8)
    color = (blue, green, red)
    Thickness = Thickness
cv2.destroyAllWindows()