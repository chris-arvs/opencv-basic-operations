import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectanle',rectangle)
cv.imshow('Circle',circle)

#bitwise AND -->intersecting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('BitwiseAND',bitwise_and)

#bitwise OR -->non intersection regions and intersection regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('BitwiseOR',bitwise_or)

#bitwise xOR -->non intersection regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('BitwiseXOR',bitwise_xor)

#bitwise NOT-->inverst binary color
bitwise_not_R = cv.bitwise_not(rectangle)
cv.imshow('RectNot',bitwise_not_R)

bitwise_not_C = cv.bitwise_not(circle)
cv.imshow('Cnot',bitwise_not_C)

cv.waitKey(0)