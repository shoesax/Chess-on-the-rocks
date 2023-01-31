import cv2
import Camera
import Processing
cam = Camera.Capture()
x=1
while(x):
    #Take picture by pressing s, press q to quit
    #cam.takePicture()

    #Reading image from folder
    image = cv2.imread("images\image.jpg")
    original = cv2.imread("images\image.jpg")

    #Applying processing
    image = Processing.processImage(image) # thresholding
    image = Processing.initialize_mask(image,original) #contouring

    #Displaying image, press any key to quit
    cv2.imshow("Board", image)
    cv2.waitKey(0)
    x=0


