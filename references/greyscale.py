import cv2
import numpy as np

image1 = cv2.imread('4.jpg')

img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh6 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('Binary Threshold', thresh1)    #imp
cv2.imshow('Adaptive thresholding', thresh2)
cv2.imshow('Binary Threshold Inverted', thresh3)
cv2.imshow('Truncated Threshold', thresh4)
cv2.imshow('Set to 0', thresh5)
cv2.imshow('Set to 0 Inverted', thresh6)


if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()