import cv2
import cv2 as cv
import time
import os


class Capture:

    def takePicture(self):
        img_counter = 0  # image_counter
        # checking if  images directory exists, if not then create images directory
        path = "images"

        CHECK_DIR = os.path.isdir(path)
        # if directory does not exist create
        if not CHECK_DIR:
            os.makedirs(path)
            print(f'"{path}" Directory is created')
        else:
            print(f'"{path}" Directory already exists.')


        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        time.sleep(1) #warms up camera

        while True:
            _,frame = cap.read()
            cv.imshow("frame", frame)

            key = cv.waitKey(1)

            if key == ord("q"):
                 break
            if key == ord("s"):
                img_name = "game{}.jpg".format(img_counter) # add _{} after image to format differently from each other
                cv2.imwrite(os.path.join(path, img_name), frame)
                print(f"saved image number {img_counter}")
                img_counter += 1  # incrementing the image counter
        cap.release()
        cv.destroyAllWindows()



