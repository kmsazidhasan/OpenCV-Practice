import cv2 as cv
import helper
from helper import *

capture = cv.VideoCapture('Videos/Trail.mp4')

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        print('Frame not found!')
        break
    
    cv.imshow('Trail', frame)
    cv.imshow('Trail_Rescaled', rescaleFrame(frame, scale = 0.25))
    
    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()