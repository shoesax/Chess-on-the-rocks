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

    #Board Initialization Processing
    image = Processing.processImage(image) # thresholding and contouring to isolate board
    image = Processing.findEdges(image)[0] #canny edge detection
    colorEdges, edges = Processing.findEdges(image) #saving edge outputs
    horizontal, vertical = Processing.findLines(edges, colorEdges) # saving detected lines
    corners= Processing.findCorners(horizontal, vertical, colorEdges) #saving corners
    squares, fullyInitialized = Processing.findSquares(corners, colorEdges) # finding squares
    image = fullyInitialized


    #Displaying image, press any key to quit
    cv2.imshow("Board", image)
    cv2.waitKey(0)
    x=0


