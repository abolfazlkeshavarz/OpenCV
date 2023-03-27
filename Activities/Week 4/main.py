import cv2 
import numpy as np

im_ulaberta = cv2.imread(r"C:\Users\Turbo\Desktop\561829.jpg")
im_ulaberta = cv2.pyrDown(im_ulaberta)
ret, threshhold =cv2.threshold(cv2.cvtColor(im_ulaberta, cv2.COLOR_BGR2GRAY),127, 255, cv2.THRESH_BINARY)
contoures, hierarchy = cv2.findContours(threshhold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(hierarchy)
print("------------------------")

# for c in contoures:
#     x,y,w,h = cv2.boundingRect(c)
#     cv2.rectangle(im_ulaberta, (x, y), (w, h), (0,255,0), 2)
#      # find minimum area
#     rect = cv2.minAreaRect(c)
#     # calculate coordinates of the minimum area rectangle
#     box = cv2.boxPoints(rect)
#     # normalize coordinates to integers
#     box = np.int0(box)
#     # draw contours
#     cv2.drawContours(im_ulaberta, [box], 0, (0,0, 255), 3)
#     # calculate center and radius of minimum enclosing circle
#     (x, y), radius = cv2.minEnclosingCircle(c)
#     # cast to integers
#     center = (int(x), int(y))
#     radius = int(radius)
#     # draw the circle
#     im_ulaberta = cv2.circle(im_ulaberta, center, radius, (0, 255, 0), 2)

cv2.drawContours(im_ulaberta, contoures, -1, (255, 0, 0), 1)
cv2.imshow('Contoures', im_ulaberta)
cv2.waitKey(0)
cv2.destroyAllWindows()