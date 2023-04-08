#this is an exercise:
import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/Weeki_spring.jpg')
LookUpTable = np.empty((1,256), np.uint8)
gama = 0.3

for i in range(255):
    LookUpTable[0, i] = np.clip(pow(i/255, gama)*255, 0, 255)
ouput = cv2.LUT(img, LookUpTable)
Linear = cv2.convertScaleAbs(img, alpha=2, beta= 85)
plt.figure(figsize=[20,10])
plt.subplot(131);plt.imshow(Linear[:,:,::-1]);plt.title('Linear approach:');
plt.subplot(132);plt.imshow(ouput[:,:,::-1]);plt.title('gamma Correction:');
plt.subplot(133);plt.imshow(img[:,:,::-1]);plt.title(('Original image:'));
plt.show()