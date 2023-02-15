import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Turbo\Desktop\Minions.jpg", 0)
cv.imwrite('Canny_Edge.png', cv.Canny(img, 200, 300))
cv.imshow('Edge', cv.imread('Canny_Edge.png'))
cv.waitKey(0)
cv.destroyAllWindows()