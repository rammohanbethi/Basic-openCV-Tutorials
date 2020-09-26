import cv2

path = r'D:\opencv tutorials\Day-1\tiger.jpg'
img  = cv2.imread(path)
print(img.shape)

width, height = 400,400
ImgResize=cv2.resize(img,(width,height))
print(ImgResize.shape)


cv2.imshow("Tiger",img)
cv2.imshow("Tiger Image",ImgResize)

cv2.waitKey(0)