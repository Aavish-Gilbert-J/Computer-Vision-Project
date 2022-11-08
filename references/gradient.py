import cv2 as cv
import numpy as np

img= cv.imread('4.jpg')

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#laplacian
lap=cv.Laplacian(gray, cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)
cv.waitKey(0)

#sobel gradient managing representation
sobelx=cv.Sobel(gray, cv.CV_64F,1,0)
sobely=cv.Sobel(gray, cv.CV_64F,0,1)
combined=cv.bitwise_or(sobelx, sobely)

cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)
cv.imshow('combined', combined)
cv.waitKey(0)