import cv2 as cv 
import helper
from helper import *

img = cv.imread('Photos/mosque_day.jpg') # returns a matrix 
rescaledImg = rescaleFrame(img, 0.5)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )
cv.imshow('Simple Thresholded Inverse', thresh_inv)

cv.waitKey(0)