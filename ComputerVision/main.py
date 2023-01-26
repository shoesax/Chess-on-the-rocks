import Camera
import time
import Board
import board_Recognition
c1 = Camera.Capture()

while(True):
    print("starting sleep")
    time.sleep(10)
    print("Starting  camera")
    c1.takePicture()
