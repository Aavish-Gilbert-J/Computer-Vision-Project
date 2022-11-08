import cv2 as cv

capture=cv.VideoCapture('tom.mp4')

def resizef(frame,scale=0.75):
    height=int(frame.shape[0]*scale)  
    width=int(frame.shape[1]*scale)
    dimentions=[width,height]
    return cv.resize(frame,dimentions,interpolation=cv.INTER_AREA)

    #use INTER_AREA IF THE IMAGE IS BEING REDIUCED 
    #USE INTER_CUBIC OR INTER_LINEAR IF ITS BEING ENLARGED

while True:
    istrue,frame=capture.read()

    cv.imshow('video',frame)
    cv.imshow('video resized',resizef(frame))

    if cv.waitKey(20) == ord('q'): # press q to exit.
        break

capture.release()
cv.destroyAllWindows()


