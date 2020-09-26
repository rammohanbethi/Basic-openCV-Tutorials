import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)

path = r'D:\opencv tutorials\Day-1\tiger.jpg'
img = cv2.imread(path)
#converting RGB image to Gray Scale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Blur Image
imgBlur = cv2.GaussianBlur(imgGray,(3,3),0)
#Canny Edge Detector
imgCanny = cv2.Canny(imgBlur,150,320)
#Dilation
imgDilation = cv2.dilate(imgCanny, kernel, iterations = 3)
#Erosion of image
kernel = np.ones((5,5),np.uint8)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow('image',img)
cv2.imshow('Grayscale',imgGray)
cv2.imshow('Blur Image',imgBlur)
cv2.imshow('Edge Detection Image',imgCanny)
cv2.imshow('imgDilation Image',imgDilation)
cv2.imshow('imgErodedn Image',imgEroded)

cv2.waitKey(0)