import cv2 as cv
haar_cascade = cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')

img= cv.imread('lady.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

print(f'Number of faces found = {len(faces)}')

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the output
cv.imshow('img', img)
cv.waitKey(0)





