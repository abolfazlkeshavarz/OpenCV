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
    