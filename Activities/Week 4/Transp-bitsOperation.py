import cv2
import numpy as np
import matplotlib.pyplot as plt
 
Img = cv2.imread('./images/Myself.jpg', -1)
B, G, R = cv2.split(Img)
Alpha = np.ones(Img.shape, np.uint8)
bgra = cv2.merge((B, G, R, Alpha))
print(bgra.shape)

plt.figure(figsize=[20,10])
plt.subplot(121);plt.imshow(bgra[:,:,0:3]),plt.title('Original Shape');
plt.subplot(122);plt.imshow(bgra[:,:,-1], cmap='gray'),plt.title('alpha image');
#plt.show()

print(cv2.split(bgra[:,:,3:6]))