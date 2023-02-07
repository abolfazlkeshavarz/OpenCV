import cv2 as cv
from manager import CaptureManager, WindowManger
from pathlib import Path
import random
import time

class cameo(object):
    def __init__(self):
        self._WindowManager = WindowManger('CAMEO', self.OnkeyPress)
        self._CaptureManager = CaptureManager(cv.VideoCapture(0), self._WindowManager, True)
    
    def run(self):
        """Run the Main loop"""
        self._WindowManager.CreateWindow()
        while self._WindowManager.isWindowCreated:
            self._CaptureManager.EnterFrame()
            frame = self._CaptureManager.Frame
            if frame is not None:
                pass
            self._CaptureManager.ExitFrame()
            self._WindowManager.ProcessEvent()

    def OnkeyPress(self, keycode):
        """
        space --> screenshot
        tab   --> start/stop recording cast
        esc   --> QUIT!!!
        
        """
        
        
        if keycode == 32:
            self._CaptureManager.WriteImg("ScreenShot"+time.strftime("%Y%m%d-%H%M%S")+".png")
        elif keycode == 83:
            if not self._CaptureManager.WritingVideo:
                self._CaptureManager.WritingVid('CapturedVideo.avi')
            else:
                self._CaptureManager.StopWriting()
        elif keycode == 27:
            self._WindowManager.DestroyWindow()

if __name__ == "__main__":
    cameo().run()