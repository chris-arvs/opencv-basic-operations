import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('img',img)
blank = np.zeros(img.shape[:2],dtype='uint8')
b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])    #set green and red to blank(black image) and only display blue
green = cv.merge([blank,g,blank])   #set blue and red to blank(black image) and only display green
red = cv.merge([blank,blank,r])     #set blue and green to blank(black image) and only display red

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged',merged)
cv.waitKey(0)