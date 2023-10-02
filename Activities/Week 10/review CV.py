import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

me = cv2.imread('.\Activities\Week 10\me.jpg')
any, thresh = cv2.threshold(me, 100, 255, cv2.THRESH_TRIANGLE)
countor = cv2.Canny(me, 60, 130)
rand = np.random.randint(0, 255, (1080,1920, 3), np.uint8)
#bgrImage = rand.reshape(360,1920,3)
cv2.imshow('Computer', thresh)
#cv2.imshow('edges' ,countor)
cropped_me = me[50:250, 50:250]
#cv2.imshow('cropped',cropped_me)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('me at thresh_bin_100_255.jpg', thresh)
