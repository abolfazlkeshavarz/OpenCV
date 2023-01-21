import numpy as np
import cv2 as cv

Img1 = np.zeros((3, 3), dtype=np.uint8)
print(Img1)
Img1 = cv.cvtColor(Img1, cv.COLOR_GRAY2BGR)
print(Img1)
