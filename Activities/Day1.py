import numpy as np
import cv2 as cv
import os

Img1 = np.zeros((5, 3), dtype=np.uint8)
print(Img1)
print(Img1.shape)
Img1 = cv.cvtColor(Img1, cv.COLOR_GRAY2BGR)
print(Img1)
print(Img1.shape)

ImgPC = cv.imread(r'C:\Users\Turbo\Desktop\org.jpg', cv.IMREAD_UNCHANGED)
print(ImgPC)
print(ImgPC.shape)
cv.imwrite("RGB.png",ImgPC)

ByteArray1 = bytearray(ImgPC)
print(ByteArray1)

ByteArray2 = bytearray("Hello","UTF-8")
print(ByteArray2)