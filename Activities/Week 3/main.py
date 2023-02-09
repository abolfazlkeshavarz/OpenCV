import cv2 as cv
import numpy as np
from scipy import ndimage

KernelMatrix_3x3 = np.array([[-1,-1,-1],
                             [-1, 8,-1],
                             [-1,-1,-1]])
KernelMatrix_5x5 = np.array([[-1,-1,-1,-1,-1],
                             [-1, 1, 2, 1,-1],
                             [-1, 2, 4, 2,-1],
                             [-1, 1, 2, 1,-1],
                             [-1,-1,-1,-1,-1]])

MinionIMG = cv.imread(r"C:\Users\Turbo\Desktop\Minions.jpg", 0)

MinionK3 = ndimage.convolve(MinionIMG, KernelMatrix_3x3)
MinionK5 = ndimage.convolve(MinionIMG, KernelMatrix_5x5)
Blurred = cv.GaussianBlur(MinionIMG, (7,7), 0)
Hpf = MinionIMG - Blurred
cv.imshow("Blurred", Blurred)
cv.imshow("HPF", Hpf)
cv.imshow("3x3", MinionK3)
cv.imshow("5x5", MinionK5)
cv.waitKey()
cv.destroyAllWindows()

