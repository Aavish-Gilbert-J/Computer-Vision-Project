import cv2 
img = cv2.imread("4.jpg")  
res = cv2.GaussianBlur(img,(41,11),cv2.BORDER_DEFAULT)
cv2.imshow('result.jpg', res) 
cv2.waitKey() 
cv2.destroyAllWindows()