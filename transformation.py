import cv2 as cv 
import helper
from helper import *

img = cv.imread('Photos/mosque_day.jpg') # returns a matrix 
rescaledImg = rescaleFrame(img, 0.5)

translated = translate(rescaledImg, 100, 100)

cv.imshow('Translated', translated)
cv.waitKey(0)
