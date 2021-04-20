import cv2 as cv
import helper
from helper import rescaleFrame

img_path = 'Photos\mosque_night.jpg'
img = rescaleFrame(cv.imread(img_path), 0.5)

cv.imshow('Mosque', img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

cv.waitKey(0)