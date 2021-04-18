import cv2 as cv 
import helper
from helper import *

img = cv.imread('Photos/mosque_day.jpg') # returns a matrix 
rescaledImg = rescaleFrame(img, 0.5)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

cv.waitKey(0)