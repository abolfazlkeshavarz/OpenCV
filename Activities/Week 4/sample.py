import cv2
import numpy as np
import matplotlib.pyplot as plt

# raw_zero = np.zeros((512,512,3), dtype='uint8')
# rectangle = cv2.rectangle(raw_zero, (128, 128), (384, 384), (0,0,255), -1)
# cv2.imshow('Rectangle', rectangle)
# raw_zero = np.zeros((512,512,3), dtype='uint8')
# circle = cv2.circle(raw_zero, (256, 256), 156, (0,255,0), -1)
# cv2.imshow('Circle', circle)
# raw_zero = np.zeros((512,512,3), dtype='uint8')
# line = cv2.line(raw_zero, (56,256),(456, 256), (255,0,0), 4)
# cv2.imshow('Line', line)
# cv2.waitKey()
# plt.figure(figsize=[20, 5])
# plt.subplot(131);plt.imshow(rectangle);plt.title('Rectangle');
# plt.subplot(132);plt.imshow(circle);plt.title('Circle');
# plt.subplot(133);plt.imshow(line);plt.title('Line');
# plt.show()

raw_zero = np.zeros((512,512,3), np.uint8)
pts = np.array([[256, 0], [64, 128], [448, 128]], np.int32)
pts.reshape((-1,1,2))
cv2.polylines(raw_zero, [pts], True, (0,0,255), 3)
cv2.rectangle(raw_zero,[64, 129], [448,512], (255, 0, 0), 3)
plt.imshow(raw_zero)
plt.show()


# We can convert type of image from pillow library with : <<< np.asarray(img) >>>