import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale = 0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA) 

def tranlate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    