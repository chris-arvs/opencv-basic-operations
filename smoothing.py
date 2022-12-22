import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

#Averaging
average = cv.blur(img,(3,3))    #the higher the kernel the most the blurring
cv.imshow('Average Blur',average)

#Gaussian
gauss = cv.GaussianBlur(img,(3,3),0) #(3,3) -> kernel , sigma ->0
cv.imshow('Gaussian Blur',gauss)

#Median
median = cv.medianBlur(img,3)   #higher kernel is bad
cv.imshow('Median Blur',median)

#Bilateral
bilatral = cv.bilateralFilter(img,5,15,15) #higher values are bad
cv.imshow('Bilateral',bilatral)

cv.waitKey(0)
