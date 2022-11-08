import cv2 as cv
import numpy as np

#creating blank array
blank=np.zeros((500,500,3),dtype='uint8')

#coloring the array(blank img)
blank[:]=0,255,0  #b,g,r

#shapes
cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=5)   #instead of int for thickness u can use cv.FILLED or thickness=-1
cv.imshow('white',blank)

#similarly cv.circle and cv.line for circle and line respectively

#text
cv.putText(blank,'AAVISH GILBERT',(50,50),cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,255),thickness=3)
cv.imshow('TEXT',blank)
cv.waitKey(0)