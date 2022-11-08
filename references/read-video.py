import cv2 as cv

capture=cv.VideoCapture('tom.mp4')

while True:
    istrue,frame=capture.read()

    cv.imshow('video',frame)

    if cv.waitKey(20) == ord('q'): # press q to exit.
        break

capture.release()
cv.destroyAllWindows()

