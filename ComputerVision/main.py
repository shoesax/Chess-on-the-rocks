import cv2
import Camera
import board_Recognition
c1 = Camera.Capture()

x=1
while(x):
    key = cv2.waitKey(1)
    print("Starting  camera")
    c1.takePicture()
    x=0


