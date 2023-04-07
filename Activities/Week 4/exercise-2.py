# note that i can't use the photo used in exercise 1 because it was a Personal
# Picture and the background was white by default so i used a new photo :)

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/Me.jpg', cv2.IMREAD_UNCHANGED)
cropped = img[67:331, 220:484, :]
output = np.zeros((264, 264, 4), np.uint8)
circle = np.zeros((264, 264), np.uint8)
output[:,:,0:3] = cropped
cv2.circle(circle, (132,132), 132, (255, 255, 255), -1)
output[:, :, 3] = circle
cv2.imwrite('4channel_cropped_image.png', output)
if True:
    print(True)
else:
    print(False)
