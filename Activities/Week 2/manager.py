import cv2 as cv
import numpy as np
import time

class CaptureManager(object):
    def __init__(self, capture, previewWindowManager = None, Mirrored = False):
        self.PreviewWM = previewWindowManager
        self.Mirrored = Mirrored
        self._capture = capture
        self._channel = 0
        self._FramesElapsed = 0
        self._enteredFrame = False
        self._Frame = None
        self._ImageFileName = None
        self._VideoFileName = None
        self._VideoEncoding = None
        self._VideoWriter = None
        self._StartTime = None
        self._fpsEstimate = None
    
    @property
    def channel(self):
        return self._channel
    @channel.setter
    def channel(self,Value):
        if self._channel != Value:
            self._channel = Value
            self._Frame = None
    
    @property
    def Frame(self):
        if self._enteredFrame and self._Frame is None:
             self._Frame = self._capture.retrieve(self._Frame, self._channel)
        return self._Frame
    
    @property
    def WritingImage(self):
        return self._ImageFileName is not None
    
    @property
    def WritingVideo(self):
        return self._VideoFileName is not None
    
    def EnterFrame(self):
        """Capture The Next Frame"""
        assert  not self._enteredFrame, \
        'previous entered frame had no exit frame'
        if self._capture is not None:
            self._enteredFrame = self._capture.grab()

    def ExitFrame(self):
        """Draw to the window. Write to files. Release the Frames"""
        if  self.Frame is None:
            self._enteredFrame = False
            return
        
        #Update fps estimated
        if self._FramesElapsed == 0:
            self._StartTime = time.time()
        else:
            timeElapsed = time.time() - self._StartTime
            self._fpsEstimate = self._FramesElapsed / timeElapsed
        self._FramesElapsed += 1
