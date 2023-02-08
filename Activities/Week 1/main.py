import numpy as np
import cv2 as cv
import os

#Create Matrixes 
Img1 = np.zeros((5, 3), dtype=np.uint8)
print(Img1)
print("\n")
print(Img1.shape)

## Just a test for myself:
    #Img1 = cv.cvtColor(Img1, cv.COLOR_GRAY2BGR) 
    #print(Img1)
    #print(Img1.shape)



# Input the file(image) from Computer:
ImgPC = cv.imread(r'C:\Users\Turbo\Desktop\org.jpg')
print(ImgPC)
print(ImgPC.shape)




ByteArray1 = bytearray(ImgPC)
#print(ByteArray1)




#Test UTF-8:
ByteArray2 = bytearray("Hello","UTF-8")
print(ByteArray2)




# Set a pixel color:(  -->((1,1,0),255)<-- note that 1,1,0 means pixel with coordinates(1,1) and channel B color,
# infact Its BGR, not RGB, channel 0 = Blue & channel 1 = Green & channel 2 = Red )

ImgPC.itemset((1,1,0),255) #--> set pixel wirh coordiantes(1,1) and channel B --> 255, maximum way
print(ImgPC.item(1, 1, 0)) # show the pixel with blue value


MyImg = cv.imread(r'E:\Madarek\Myself.jpg')

## delte B,R,G --> colours
#MyImg[:, :, 0] = 0
#MyImg[:, :, 1] = 0
#MyImg[:, :, 2] = 0

print(MyImg.shape) #image shape 
print(MyImg.size) #image size
print(MyImg.dtype) #Image Type

cv.imwrite('MySelf.jpg', MyImg)
cv.imshow('MySelf.jpg', MyImg)
cv.waitKey(0)
cv.destroyAllWindows()


# Capturing a Video
Video = cv.VideoCapture(r"E:\01_NewDjango_Ordookhani.avi")
fps = Video.get(cv.CAP_PROP_FPS)
print(int(fps))
size = (int(Video.get(cv.CAP_PROP_FRAME_WIDTH)), int(Video.get(cv.CAP_PROP_FRAME_HEIGHT)))
print(size)
WrottenVideo = cv.VideoWriter('Sample.avi', cv.VideoWriter_fourcc('X','V','I','D'), fps, size)

correct, frame = Video.read()
while correct:
    WrottenVideo.write(frame)
    correct, frame = Video.read()


## Capture Camera and write the video
Camera = cv.VideoCapture(0)
Fps = Camera.get(cv.CAP_PROP_FPS)
print(Fps)
Size = (int(Camera.get(cv.CAP_PROP_FRAME_WIDTH)), int(Camera.get(cv.CAP_PROP_FRAME_HEIGHT)))
print(Size)
WrottenCameraVid = cv.VideoWriter('My Cam.avi', cv.VideoWriter_fourcc('X', 'V', 'I', 'D'), Fps, Size)
success, Frame = Camera.read()
FrameNum = 15 * Fps  
while success and FrameNum != 0:
    WrottenCameraVid.write(Frame)
    success, Frame = Camera.read()
    FrameNum -= 1
