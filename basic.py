import cv2 as cv
import helper
from helper import rescaleFrame

img_path = 'Photos\mosque_night.jpg'
img = rescaleFrame(cv.imread(img_path), 0.5)

# GrayScale from RGB
gray = cv.cvtColor(img, code= cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)

# Blurring an Image
blur = cv.GaussianBlur(img, ksize=(5,5), sigmaX=cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascading
canny = cv.Canny(img, 150, 300)
cv.imshow('Edge_Canny', canny )

dilate = cv.dilate(canny, (3, 3), iterations=3)
cv.imshow('Edge_Dilate', dilate)

erode = cv.erode(dilate, (3, 3), iterations=3)
cv.imshow('Edge_Erode', erode)

# Cropping an Image
crop = img[200:400, 500:700]
cv.imshow('Cropped', crop)

cv.waitKey(0)
