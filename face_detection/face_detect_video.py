import cv2 as cv
haar_cascade = cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')

capture=cv.VideoCapture(0)

while True:
    istrue,frame=capture.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv.imshow('video',frame)

    if cv.waitKey(20) == ord('q'): # press q to exit.
        break

capture.release()
cv.destroyAllWindows()