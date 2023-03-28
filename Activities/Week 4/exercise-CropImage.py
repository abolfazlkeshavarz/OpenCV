import cv2 
import numpy as np # we didn't use this library at this exercise!!
import matplotlib.pyplot as plt

Img = cv2.imread("./images/Myself.jpg")
plt.imshow(Img)
plt.show()
print(Img.shape)
#Height, Width = Img.shape[:2]
Cropped = Img[10:200, 50:200, ::-1]
plt.imshow(Cropped)
plt.show()
# cv2.imshow("Me", Img)
# cv2.waitKey()
# cv2.destroyAllWindows()