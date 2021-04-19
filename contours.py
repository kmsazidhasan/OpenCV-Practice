import cv2 as cv
import helper
from helper import rescaleFrame

img_path = 'Photos\mosque_night.jpg'
img = rescaleFrame(cv.imread(img_path), 0.5)

gray = cv.cvtColor(img, code= cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Edge_Canny', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)