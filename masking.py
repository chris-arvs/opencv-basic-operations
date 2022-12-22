import  cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats2.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank image',blank)
#Mask and Image in which mask will apllied MUST have the same dimentions
#--------- Creating a mask ---------------------------------------------------------
mask = cv.circle(blank.copy(), (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
cv.imshow('Mask', mask)
#--------- -------------------------------------------------------------------------
#------------------------- Use the mask on the image -------------------------------
masked = cv.bitwise_and(img,img,blank,mask=mask)
cv.imshow('Masked Image',masked)
#--------- -------------------------------------------------------------------------
#--------- Creating a mask from a circle and a rectangular  ---------------------------------------------------------
circle = cv.circle(blank.copy(), (img.shape[1] // 2 + 45, img.shape[0] // 2), 100, 255, -1)
rectangular = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
weird_shape = cv.bitwise_and(circle, rectangular)
cv.imshow('Weird shape',weird_shape)
#------------------------- Use weird shape as mask on the image -------------------------------
masked1 = cv.bitwise_and(img,img,blank,mask = weird_shape)
cv.imshow('Weird Shape Masked Image',masked1)
cv.waitKey(0)