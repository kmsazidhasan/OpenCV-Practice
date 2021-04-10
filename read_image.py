import cv2 as cv 
import helper
from helper import *

img = cv.imread('Photos/mosque_day.jpg') # returns a matrix 

cv.imshow('Mosque', img) # takes window name and matrix as input 
cv.imshow('Mosque_Rescaled', rescaleFrame(img, 0.5)) 
cv.waitKey(0) # Waiting for a key press, 0 means it will wait infinitely. Returns the ASCII value of pressed key.

