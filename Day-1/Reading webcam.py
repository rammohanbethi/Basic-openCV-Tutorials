import cv2

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
#cap.set(3, frameWidth)
#cap.set(4, frameHeight)

while True:
    sucess, img = cap.read()
    cv2.imshow("video", img)
    #Next we are going to show our frame and add a delay so we can see the output.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    