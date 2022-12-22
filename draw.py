import cv2 as cv
import numpy as np

#create a blank image to draw
blank = np.zeros((500,500,3),dtype='uint8') #(Width,Height,Channels)

cv.imshow('blank',blank)
#1. Paint image certain colour
blank[:] = 0,255,0
cv.imshow("Green",blank)

blank[200:300,300:400] = 0,0,255
cv.imshow('PartianRed',blank)

#2. draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)   #from 0,0 to 250,250
cv.imshow('Rectangle-250x250',blank)

cv.rectangle(blank,(0,0),(250,400),(0,255,0),thickness=2)   #from 0,0 to 250,400
cv.imshow('Rectangle-250x400',blank)

cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,255,0),thickness=-1) #negative value does the filling
#img.shape[0] -> width
#img.shape[1] -> height
cv.imshow('Rectangle',blank)

#3. draw circle
cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),40,(0,0,255),thickness=3)
cv.imshow('Circle',blank)
#fill the circle by giving thickness=-1
cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),40,(0,0,255),thickness=-1)
cv.imshow('Circle-filled',blank)

#4. draw line
cv.line(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(255,255,255),thickness=3)
cv.imshow('Line',blank)

#5.Write text on an image
cv.putText(blank,'Hello,my name is Chris',(0,255),cv.FONT_HERSHEY_TRIPLEX,0.5,(0,0,0),thickness=2)
cv.imshow('Text',blank)
cv.waitKey(0)