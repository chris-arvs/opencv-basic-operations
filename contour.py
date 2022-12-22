import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('Grey',gray)
#img.shape[:2] means everything before second argument
blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

#----------- Method 1 to find contours ------------------------------------
# #By blurring the image we reduce drasticly the contours find in the image
# blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('Blured',blur)
#
# canny = cv.Canny(blur,125,175)   #125 and 175 are threshold values
# cv.imshow('Canny Edges',canny)
#--------------------------------------------------------------------------

#----------- Method 2 to find contours ------------------------------------
#every pixel with intensity less than 125 becomes 0(black)
#every pixel with intensity above 125 becomes 255(white)
ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresholding image',thresh)
#--------------------------------------------------------------------------

#contours are python lists which has all the contours found in the image
contours ,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')    #length of list
cv.waitKey(0)