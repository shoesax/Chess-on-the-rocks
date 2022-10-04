import numpy as np
import cv2

# Creating connection to Logitech Camera
cap = cv2.VideoCapture(1)

while(True):
    # Getting a frame from camera
    ret, frame = cap.read()

    # Converts RGB image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Editing image for image segmentation via k-means
    Z = frame.reshape((-1, 3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 4   # 4 k-mean clusters

    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Converting back into uint8
    center = np.uint8(center)
    res = center[label.flatten()]

    res2 = res.reshape((frame.shape))
    cv2.imshow('res2', res2)


    # Display the resulting frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Releases video capture, closes feed window
cap.release()
cv2.destroyAllWindows()
