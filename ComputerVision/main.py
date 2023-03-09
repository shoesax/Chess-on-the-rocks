import cv2
import Camera
import Processing
import Movement
import chess
cam = Camera.Capture()

#Take picture by pressing s, press q to quit
# cam.takePicture()

#TAKING EMPTY BOARD PICTURE
cam.boardPicture()

#Reading image from folder
image = cv2.imread("images\mygame\move.jpg")

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

#CREATING ENGINE BOARD
engboard = chess.Board()

#STUFF TO SHOW

# cv2.imshow("Board", board)
# cv2.waitKey(0)

#TAKING INITIAL BOARD STATE PICTURE
print("Take a picture of the initial board setup.")
cam.movePicture(0)
previous = cv2.imread("images\mygame\move0.jpg")
previous = Processing.processImage(previous)
previous = Processing.findEdges(previous)[0]

c=1
while(True):
    #HARDWARE MOVE
    while (True):
        cam.movePicture(c)
        current = cv2.imread("images\mygame\move{}.jpg".format(c))
        current = Processing.processImage(current)
        current = Processing.findEdges(current)[0]
        if (chess.Move.from_uci(myBoard.determineChanges(previous, current)) not in engboard.legal_moves):
            print(myBoard.determineChanges(previous, current)+"Move is not valid, retake picture.")
        else:
            break

    print("Hardware Move:" + myBoard.determineChanges(previous, current))
    engboard.push_san(myBoard.determineChanges(previous, current))
    print(engboard)
    if(engboard.is_checkmate() == True):
        print("Checkmate! White Wins!")
        break
    if(engboard.is_stalemate()==True):
        print("Stalemate!")
        break

    #PC MOVE
    while(True):
        userMove = input("Enter the PC user move: ")
        if (chess.Move.from_uci(userMove) not in engboard.legal_moves):
            print("Move is not valid.")
        else:
            break
    engboard.push_san(userMove)
    print(engboard)
    if (engboard.is_checkmate() == True):
        print("Checkmate! Black Wins!")
        break
    if (engboard.is_stalemate() == True):
        print("Stalemate!")
        break

    previous = current
    c += 1




