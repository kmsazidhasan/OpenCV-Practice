import cv2 as cv
import numpy as np

frame = np.zeros((500, 500, 3), dtype = np.uint8)
frame[:] = 0, 0, 255    # broadcasting
cv.rectangle(frame, (0, 0), (frame.shape[1]//2, frame.shape[0]//2 ), (0, 255, 0), thickness = cv.FILLED)  # args -> frame, diag initial point, diag end point, line thickness = (-1) alternate 
cv.imshow('Rectangle', frame)
cv.circle(frame, (frame.shape[1]//2, frame.shape[0]//2 ), 50, (255, 0, 0), thickness = -1)
cv.imshow('Circle', frame)
cv.line(frame, (0, 0), (frame.shape[1]//2, frame.shape[0]//2 ), color=(255, 255, 255), thickness=3)
cv.imshow('Line', frame)
cv.waitKey(0)
