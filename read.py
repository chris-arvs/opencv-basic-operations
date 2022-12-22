import cv2 as cv

#Reading images
img = cv.imread('Resources/Photos/cat_large.jpg')
cv.imshow('test1',img)

#Reading videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

#read video frame by frame
while True:
    isTrues, frame = capture.read()
    cv.imshow('Video',frame)

   if cv.waitKey(20) & 0xFF==ord('d'):      # to stop video press d
        break

capture.release()
cv.destroyAllWindows()

