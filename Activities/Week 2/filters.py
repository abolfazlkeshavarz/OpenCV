import utils
import cv2 as cv 
import numpy as np

def strokeEdges(src, dst, blurKsize = 7, edgeKsize = 5):
    if blurKsize >= 3:
        blurredSrc = cv.medianBlur(src, blurKsize)
        graySrc = cv.cvtColor(blurredSrc, cv.COLOR_BGR2GRAY)
    else:
        graySrc = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.Laplacian(graySrc, cv.CV_8U, graySrc, edgeKsize)
    normallizedIA = (1.0 / 255) * (255 - graySrc)
    channels = cv.split(src)
    for channel in channels:
        channel[:] = channel * normallizedIA
    cv.merge(channels, dst)
