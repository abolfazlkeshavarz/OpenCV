import cv2 
import numpy as np
import matplotlib.pyplot as plt

prim_img = cv2.imread('./images/Tech.jpg', cv2.IMREAD_UNCHANGED)
sec_img = cv2.imread('./images/Code-binary.jpg', cv2.IMREAD_UNCHANGED)

hund = np.ones(prim_img, np.uint8) * 100
array1 = np.array([[155,156],[157,158]], np.uint8)
output = array1 + hund
print(output)
array1 = array1.astype('uint16')
output = array1 + hund
output = np.minimum(output, 255)
output = output.astype(dtype='uint8')
print(output)
print(hund)

added = cv2.add(prim_img, hund)
subt = cv2.subtract(sec_img, hund)
plt.figure(figsize=[20,5])
plt.subplot(121);plt.imshow(added[:,:,::-1]);plt.title('Added');
plt.subplot(122);plt.imshow(subt[:,:,::-1]);plt.title('Subtracted');
plt.show()