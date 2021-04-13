import cv2 as cv
import helper
from helper import rescaleFrame

img_path = 'Photos\mosque_night.jpg'
img = rescaleFrame(cv.imread(img_path), 0.5)

# GrayScale from RGB
gray = cv.cvtColor(img, code= cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)
cv.waitKey(0)