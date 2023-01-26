import cv2 as cv
import imutils
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


        cap = cv.VideoCapture(0)

        while True:
            _,frame = cap.read()

            #image, board_detected = detect_checker_board(frame, gray, criteria, CHESS_BOARD_DIM)
            #frame = frame.array
            #resized = imutils.resize(frame, height = 400, width = 400)
            cv.imshow("frame", frame)
            #cv.imshow("copyFrame", copyFrame)

            key = cv.waitKey(1)

            if key == ord("q"):
                break
            if key == ord("s"):
                cv.imwrite(f"{image_dir_path}/image{n}.png", frame)

                print(f"saved image number {n}")
                n += 1  # incrementing the image counter
        cap.release()
        cv.destroyAllWindows()

        print("Total saved Images:", n)
