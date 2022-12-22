import cv2 as cv

#function to resize img or frame (video,live camera,image)
def rescaleFrame(frame,scale=0.75):
    width =int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    dimentions = (width,height)

    return  cv.resize(frame,dimentions,interpolation=cv.INTER_AREA)

# #its only for live videos(like web cams)
# def changeRes(width,height):
#     capture.set(3,width)    #3 is reference for width
#     capture.set(4,height)   #4 is reference for height


# image resize
img = cv.imread('Resources/Photos/cat.jpg')
resized_img = rescaleFrame(img)
cv.imshow('res_img',resized_img)

#read video frame by frame
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
   isTrue, frame = capture.read()
   frame_resized = rescaleFrame(frame,scale=0.2)
   #cv.imshow('Video',frame)
   cv.imshow('Video',frame_resized)
   if isTrue:
       cv.imshow('Video', frame)
       if cv.waitKey(20) & 0xFF==ord('d'):
          break
   else:
       break

#capture.release()
capture_live.release()
cv.destroyAllWindows()

