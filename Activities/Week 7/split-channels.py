import cv2
import numpy as np
import matplotlib.pyplot as plt

Img_alberta = cv2.imread('./images/ualberta.jpeg')
Img_alberta = cv2.pyrDown(Img_alberta)
B, G, R =cv2.split(Img_alberta)
plt.figure(figsize=[15,10])
plt.subplot(221);plt.imshow(B, cmap = 'gray');plt.title('Blue Channel');
plt.subplot(222);plt.imshow(G, cmap = 'gray');plt.title('Green Channel');
plt.subplot(223);plt.imshow(R, cmap = 'gray');plt.title('Red Channel');
plt.subplot(224);plt.imshow(Img_alberta[:,:,::-1]);plt.title('All Channels');
plt.show()