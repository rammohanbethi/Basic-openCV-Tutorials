import cv2

frameWidth = 640
frameHeight = 360

cap = cv2.VideoCapture(r'D:\opencv tutorials\test.mp4')
while True:
    sucess, img = cap.read()
    #img = cv2.resize(img,(frameWidth,frameHeight))
    cv2.imshow("video", img)
    #Next we are going to show our frame and add a delay so we can see the output.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    