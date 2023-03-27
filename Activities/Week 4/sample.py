import cv2
import numpy as np
img = cv2.pyrDown(cv2.imread(r'E:\GitHub\OpenCV\Activities\Week 4\ualberta.jpeg', cv2.IMREAD_UNCHANGED))
ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127,
255, cv2.THRESH_BINARY)
contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
