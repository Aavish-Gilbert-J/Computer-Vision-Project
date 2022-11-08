import cv2 as cv

img = cv.imread("4.jpg")  

#average blur
blur = cv.blur(img,(3,3))
cv.imshow('average blur', blur) 

#gaussian blur
blur1 = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('gaussian blur', blur1) 

#median blur           #good technique
blur2 = cv.medianBlur(img,3)
cv.imshow('median blur', blur2) 

#bilateral blur         #best technique
blur3=cv.bilateralFilter(img,10,35,25)
cv.imshow('bilateral blur', blur3 )


cv.waitKey(0)
cv.destroyAllWindows()
