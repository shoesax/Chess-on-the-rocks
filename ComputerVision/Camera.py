import cv2
import cv2 as cv
import imutils
import time
import os


class Capture:

    def takePicture(self):
        n = 0  # image_counter

        # checking if  images directory exists, if not then create images directory
        image_dir_path = "images"

        CHECK_DIR = os.path.isdir(image_dir_path)
        # if directory does not exist create
        if not CHECK_DIR:
            os.makedirs(image_dir_path)
            print(f'"{image_dir_path}" Directory is created')
        else:
            print(f'"{image_dir_path}" Directory already exists.')


        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        time.sleep(1) #warms up camera

        while True:
            _,frame = cap.read()

            #processing
            resized = imutils.resize(frame, width=400, height=400)
            gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
            adaptiveThresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 125, 1)


            cv.imshow("frame", adaptiveThresh)


            key = cv.waitKey(1)

            if key == ord("q"):
                 break
            if key == ord("s"):
                print(f"saved image number {n}")
                n += 1  # incrementing the image counter
        cap.release()
        cv.destroyAllWindows()



