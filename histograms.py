import cv2 as cv
import  numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blank = np.zeros(img.shape[:2],dtype='uint8')
circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
mask = cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('Mask',mask)
#GRscale hist
# gray_hist = cv.calcHist([gray],[0], mask,[256],[0,256])
#
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.savefig('f1.png')
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

cv.waitKey(0)