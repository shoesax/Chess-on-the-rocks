import cv2
import time
import imutils

class Camera:

	def __init__(self):
		self.cam = cv2.VideoCapture(0) # setting camera input source

	def takePicture(self):

		# allows camera to warm up
		time.sleep(1)

		# takes picture
		result, image = self.cam.read()

		# processing image
		image = image.array
		resized = imutils.resize(image, height = 400, width = 400)

		return resized

