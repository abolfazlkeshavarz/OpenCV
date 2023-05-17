import cv2
import numpy as np

cap = cv2.VideoCapture(0)
gama = 0.3

def gama_correction(img):
    lookuptable = np.empty((1, 256), np.uint8)
    for i in range(256):
        lookuptable[0, i] = np.clip(pow(i / 255.0, gama) * 255.0 , 0, 255)
    output = cv2.LUT(img, lookuptable)
    return output

while True:
    ret, frame = cap.read()
    if ret == False:
        print("couldn't find or handle webcam!!!")
        break
    cv2.imshow('Original', frame)
    gamma = gama_correction(frame)
    cv2.imshow('Gamma', gamma)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

# frame.release()
# gamma.release()
cv2.destroyAllWindows()