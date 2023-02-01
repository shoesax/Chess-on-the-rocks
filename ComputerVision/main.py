import cv2
import Camera
import Processing
cam = Camera.Capture()
x=1
while(x):
    #Take picture by pressing s, press q to quit
    #cam.takePicture()

    #Reading image from folder
    image = cv2.imread("images\image3.jpg")

    #Applying processing
    image = Processing.processImage(image) # thresholding and contouring to isolate board
    image = Processing.findEdges(image) #canny edge detection

    #Displaying image, press any key to quit
    cv2.imshow("Board", image)
    cv2.waitKey(0)
    x=0


