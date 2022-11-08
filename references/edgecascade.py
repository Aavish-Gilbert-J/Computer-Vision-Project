import cv2

def canny_webcam():

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()  

        frame = cv2.GaussianBlur(frame, (3, 3), 1.41)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        edge = cv2(frame, 75, 175)

        cv2.imshow('Canny Edge', edge)

        if cv2.waitKey(20) == ord('q'):  #press q to exit.
            break

canny_webcam()

#you can use dialate and erode sub modules of cv2 to further process the canny image
#dialate to increase size of the edge
#erode to getback the image