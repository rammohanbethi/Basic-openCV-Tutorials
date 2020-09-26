#import our library which is cv2 (CV stands for computer vision).
import cv2
#Next we are going to load our image using imread
img = cv2.imread('tiger.jpg')
#now give window name and display the image using imshow function
cv2.imshow('Animal',img)  #animal is window frame name and img is stored image variable
 #using cv2.waitkey and we will add the delay in milliseconds so for example I can say 1000
cv2.waitKey(0)