####################Allows to verify if camera is functioning and take picture on button click#########
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
img_counter = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break
    elif cv2.waitKey(1) == ord('i'):
        img_name = "image.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("screenshot taken")
        img_counter+=1

cap.release()
cv2.destroyAllWindows()