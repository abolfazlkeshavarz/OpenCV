import cv2 as cv
import numpy as np

#img = cv.imread(r"C:\Users\Turbo\Desktop\Minions.jpg", 0)
Img = np.zeros((1000, 1000), dtype=np.uint8)
Img[50:950 , 50:950] = 255

ret, thresh = cv.threshold(Img, 127, 255, 0)
contoures, hireachy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
color = cv.cvtColor(Img, cv.COLOR_GRAY2BGR)
Img = cv.drawContours(color, contoures, -1, (0,255,0), 2)
cv.imshow("NEW", Img)
print(np.shape(thresh))
cv.waitKey(0)
cv.destroyAllWindows()
