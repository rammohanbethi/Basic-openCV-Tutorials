import cv2

path = r'D:\opencv tutorials\Day-1\tiger.jpg'
img  = cv2.imread(path)
print(img.shape)
#frame size
width, height = 400,400
ImgResize=cv2.resize(img,(width,height))
print(ImgResize.shape)
#image cropping
imgCropped = img[0:120,200:240]
#resize the cropped image
imCropResize  = cv2.resize(imgCropped,(img.shape[1],img.shape[0]))

cv2.imshow("Tiger",img)
cv2.imshow("Tiger Image",ImgResize)
cv2.imshow("Tiger Image Cropped",imgCropped)
cv2.imshow("Tiger Image ResizeCropped",imCropResize)
 

cv2.waitKey(0)