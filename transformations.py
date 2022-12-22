import  cv2 as cv
import numpy as np
img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park',img)

#translation - to shift image up,down,l;eft,right
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])        #translation Matrix -- a list with two list inside
    dimentions = (img.shape[1],img.shape[0])        #dsize -- image size
    return cv.warpAffine(img,transMat,dimentions)
# -x -->shift image Left
# -y -->shift image Up
#  x -->shift image Right
#  y -->shift image Down

translated = translate(img,100,100) #--shift image Right and Down by 100pixels
cv.imshow('transalted',translated)

translated = translate(img,-100,-100) #--shift image Right and Down by 100pixels
cv.imshow('transalted',translated)

translated = translate(img,-100,100) #--shift image Right and Down by 100pixels
cv.imshow('transalted',translated)

#Rotation
def rotate(img,angle,rotPoint=None):
    (width,height) = img.shape[:2]      #select everything before 2nd element
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMap = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimentions = (width,height)
    return cv.warpAffine(img,rotMap,dimentions)

rotated = rotate(img,-45)              #rotate 45 degrees -- minus (-45) means to rotate clockwise
cv.imshow('Rotated',rotated)
rotated_rotated = rotate(rotated,-90)
cv.imshow('Rotate rotated',rotated_rotated)

#Resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Flipping
# 0 -->flip verticly
# 1 -->flip horizontaly
#-1 -->flip verticly and horizontaly
flip = cv.flip(img,0)
cv.imshow('FlipVert',flip)

flip = cv.flip(img,1)
cv.imshow('FlipHor',flip)

flip = cv.flip(img,-1)
cv.imshow('FlipHorVert',flip)

#Cropping
cropped = img[200:400,300:400]
cv.imshow('Crop',cropped)
cv.waitKey(0)