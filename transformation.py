import cv2 as cv 
import helper
from helper import *

img = cv.imread('Photos/mosque_day.jpg') # returns a matrix 
rescaledImg = rescaleFrame(img, 0.5)

rotated = rotate(rescaledImg, 45)
cv.imshow('Rotated', rotated)

translated = translate(rescaledImg, 100, 100)
cv.imshow('Translated', translated)

flip = cv.flip(rescaledImg, -1)
cv.imshow('Flip', flip)

cv.waitKey(0)