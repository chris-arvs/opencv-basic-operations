import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Simple Thresholding
threshold, thresh =cv.threshold(gray,150,255,cv.THRESH_BINARY) #threshol ->125 maxVal->255 , 0 below 125 , 1 above 125
cv.imshow('Simple Thresholded',thresh)

#Inverse thresholding
threshold, thresh_inv =cv.threshold(gray,150,255,cv.THRESH_BINARY_INV) #threshol ->125 maxVal->255 , 0 below 125 , 1 above 125
cv.imshow('Simple Thresholded Inverse',thresh_inv)

#Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3) #method->mean, block size(kernel) ->11 , C(for fine tuning)->3
cv.imshow('Adaptive Thresholding',adaptive_thresh)
cv.waitKey(0)
