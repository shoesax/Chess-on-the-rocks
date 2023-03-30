import cv2
import Camera
import Processing
import Movement
import chess
import pygame
import ChessEngine as engine


cam = Camera.Capture()
gs = engine.GameState()

chess_files = { "a":0, "b": 1, "c": 2,"d": 3, "e": 4, "f":5, "g": 6, "h": 7}
chess_ranks = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7}

DIMENSION = 8
HEIGHT = 800
WIDTH = HEIGHT
Square_Size = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def map_move(moves):
    first_square = moves[0] + moves[1]
    second_square = moves[2] + moves[3]

    first_move = str(chess_files[first_square[0]]) + str(chess_ranks[first_square[1]])
    second_move = str(chess_files[second_square[0]]) + str(chess_ranks[second_square[1]])

    return first_move, second_move

def draw_Board(screen):
    colors = [pygame.Color("white"), pygame.Color("blue")]

    for r in range(DIMENSION):
        for c in range(DIMENSION):
           color = colors[ ( (r+c)%2 )] 
           pygame.draw.rect(screen,color, pygame.Rect(c*Square_Size, r*Square_Size, Square_Size, Square_Size))

def draw_pieces(screen,board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], pygame.Rect(col*Square_Size, row*Square_Size, Square_Size, Square_Size))

def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if (piece != "--"):
                if( piece[0] == "b"):   
                    screen.blit(IMAGES[piece], pygame.Rect(col*Square_Size, row*Square_Size, Square_Size, Square_Size))

def load_Images():

    list_Pieces = ['wp','wR','wN','wB','wQ','wK','bp','bR','bN','bB','bQ','bK']
    for piece in list_Pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("pieceImages/"+piece+".png"), ( Square_Size ,Square_Size))

def draw_software_board(move):

    # first_move, second_move = map_move(move)
    # gs.board[int(second_move[1])][int(second_move[0])] = gs.board[int(first_move[1])][int(first_move[0])]
    # gs.board[int(first_move[1])][int(first_move[0])] = "--"

    running = True
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    while(running):
        
        # print("hello")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
       
        if(running):
            # cam.takePicture()
            draw_Board(screen)
            draw_pieces(screen,gs.board)
            clock.tick(MAX_FPS)
            pygame.display.flip()

#Take picture by pressing s, press q to quit
# cam.takePicture()

#Reading image from folder
image = cv2.imread("images\gametest2\move.jpg")
load_Images()

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

p=0
c=1
pygame.init()
# screen = pygame.display.set_mode((WIDTH,HEIGHT))
while(True):
    #MOVE IMAGES
    previous = cv2.imread("images\gametest2\move{}.jpg".format(p))
    previous = Processing.processImage(previous)
    previous = Processing.findEdges(previous)[0]

    current = cv2.imread("images\gametest2\move{}.jpg".format(c))
    current = Processing.processImage(current)
    current = Processing.findEdges(current)[0]

    #HARDWARE MOVE
    while (True):
        if (chess.Move.from_uci(myBoard.determineChanges(previous, current)) not in engboard.legal_moves):
            print("Move is not valid.")
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
    draw_software_board(userMove)
    print(engboard)
    if (engboard.is_checkmate() == True):
        print("Checkmate! Black Wins!")
        break
    if (engboard.is_stalemate() == True):
        print("Stalemate!")
        break

    p += 1
    c += 1



