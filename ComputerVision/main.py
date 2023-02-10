import cv2
import Camera
import Processing
import Movement
cam = Camera.Capture()
x=1
while(x):
    #Take picture by pressing s, press q to quit
    #cam.takePicture()

    #Reading image from folder
    initial = cv2.imread("images\move\move.jpg")
    image = cv2.imread("images\move\move.jpg")

    #Board Initialization Processing
    print("Initializing board")
    image = Processing.processImage(image) # thresholding and contouring to isolate board
    image = Processing.findEdges(image)[0] #canny edge detection
    colorEdges, edges = Processing.findEdges(image) #saving edge outputs
    horizontal, vertical = Processing.findLines(edges, colorEdges) # saving detected lines
    corners= Processing.findCorners(horizontal, vertical, colorEdges) #saving corners
    squares, fullyInitialized = Processing.findSquares(corners, colorEdges) # finding squares
    image = fullyInitialized
    print("Board fully initialized")

    #CRATING BOARD
    myBoard = Movement.Board(squares)
    myBoard.draw(image)

    #MOVE IMAGES
    previous = cv2.imread("images\move\move0.jpg")
    previous = Processing.processImage(previous)
    previous = Processing.findEdges(previous)[0]
    current = cv2.imread("images\move\move1.jpg")
    current = Processing.processImage(current)
    current = Processing.findEdges(current)[0]

    #MOVE OUTPUT
    print(myBoard.determineChanges(previous, current))


    #Displaying image, press any key to quit
    imshow = cv2.imshow("Initial", initial)
    cv2.imshow("Board", image)
    cv2.waitKey(0)
    x=0


