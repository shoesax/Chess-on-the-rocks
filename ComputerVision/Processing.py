import cv2
import imutils

def processImage(image):
    resized = imutils.resize(image, width=400, height=400) # resizing image
    gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY) #applying grayscale
    adaptiveThresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 125, 1) #thresholding
    return adaptiveThresh
