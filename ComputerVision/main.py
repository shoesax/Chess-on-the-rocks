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
    image = cv2.imread("images\move\move2.jpg")

    #Board Initialization Processing
    print("Initializing board")
    image = Processing.processImage(image) # thresholding and contouring to isolate board
    image = Processing.findEdges(image)[0] #canny edge detection
    colorEdges, edges = Processing.findEdges(image) #saving edge outputs
    horizontal, vertical = Processing.findLines(edges, colorEdges) # saving detected lines
    corners= Processing.findCorners(horizontal, vertical, colorEdges) #saving corners
    squares, fullyInitialized = Processing.findSquares(corners, colorEdges) # finding squares
    board = fullyInitialized
    print("Board fully initialized")

    #CREATING BOARD
    myBoard = Movement.Board(squares)
    myBoard.assignState()
    myBoard.draw(image)

    #MOVE IMAGES
    previous = cv2.imread("images\move\move0.jpg")
    previous = Processing.processImage(previous)
    previous = Processing.findEdges(previous)[0]

    current = cv2.imread("images\move\move1.jpg")
    current = Processing.processImage(current)
    current = Processing.findEdges(current)[0]

    #MOVE OUTPUT
    cv2.imshow("Board", board)
    cv2.imshow("prev", previous)
    cv2.imshow("curr", current)
    cv2.waitKey(0)
    print(myBoard.determineChanges(previous, current))
    print(myBoard.boardMatrix)

    x=0


