#canny

import cv2

import numpy as np


def canny_webcam():
    "Live capture frames from webcam and show the canny edge image of the captured frames."

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()  

        blank=np.zeros((frame.shape[:]),dtype='uint8')

        grey=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        blur=cv2.GaussianBlur(grey,(3,3),cv2.BORDER_DEFAULT)

        canny=cv2.Canny(blur,75,225)

        contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(blank,contours,-1,(0,0,255),2)

        cv2.imshow('contour',blank)

        

        if cv2.waitKey(20) == ord('q'):  # Introduce 20 milisecond delay. press q to exit.
            break

canny_webcam()