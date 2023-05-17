import cv2
import numpy as np
from matplotlib import pyplot as plt

video = cv2.VideoCapture(r'/home/abolfazl/Downloads/1080p-video.mp4')

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

print(width)
print(height)
out = cv2.VideoWriter('test.avi', cv2.VideoWriter_fourcc(*'MJPG'), video.get(cv2.CAP_PROP_FPS), (width, height), False)
while True:
    ret, frame = video.read()
    if ret == True:
        cv2.putText(frame, "FPS:{}".format(fps), (40, 40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2 ,(255, 255, 255), 3)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(gray)
    else:
        print("Done")
        break

video.release()
out.release()
cv2.destroyAllWindows()