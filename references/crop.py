import cv2 as cv
img=cv.imread('4.jpg')
cropped=img[50:500,50:550]  #use this trick to slice the array
cv.imshow('crop',cropped)
cv.waitKey(0)