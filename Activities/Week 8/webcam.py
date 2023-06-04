import cv2
Cap = cv2.VideoCapture(0)
while True:
    _, frame = Cap.read()
    cv2.imshow("webcam", frame)
    key = cv2.waitKey(1) & 0XFF
    if key == 27:
        break 
cv2.destroyAllWindows()