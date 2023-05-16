import cv2
import numpy as np

window_title = 'Trackbar Brush'
alpha_max = 100
def trackbar(val):
    alpha = val/alpha_max
    beta = (1.0 - alpha_max)
    dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)
    cv2.imshow(window_title, dst)
src1 = cv2.imread('./images/8cell.png')
src2 = cv2.imread('./images/200px.jpeg')
cv2.namedWindow('Trackbar Brush')
trackbar_name = 'alpha'
cv2.createTrackbar(trackbar_name, window_title, 0, alpha_max, trackbar)
trackbar(50)
cv2.waitKey()
cv2.destroyAllWindows()