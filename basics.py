import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('park',img)

#convert to greyscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT) # (3,3) is the kernel - it must be an odd number - the biggest the kernel the most the blur
cv.imshow('Blur',blur)

#Edge Cascade
# canny = cv.Canny(img,125,175)
# cv.imshow('Canny_Edges',canny)

canny = cv.Canny(blur,125,175) #to get rid of the edges , blur the image givven in Canny
cv.imshow('Canny_Edges',canny)

#Dilate the Image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dialated',dilated)
#Erode the image
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

#Resize
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC) #interpolation (cubic,linear ,nearest,area etc...)
cv.imshow('Resized',resized)
#Cropping
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)