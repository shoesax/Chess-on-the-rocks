import cv2
import Camera
import Processing
import Movement
import chess
import ChessEngine as engine
import sys
import pygame as p

p.init()
p.display.init()

cam = Camera.Capture()
clock = p.time.Clock()
gs = engine.GameState()

WIDTH = 1000
HEIGHT = WIDTH
DIMENSION = 8
MAX_FPS = 15
Square_Size = HEIGHT // DIMENSION

chess_files = { "a":0, "b": 1, "c": 2,"d": 3, "e": 4, "f":5, "g": 6, "h": 7}
chess_ranks = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7}

IMAGES = {}

def map_move(moves):
    first_square = moves[0] + moves[1]
    second_square = moves[2] + moves[3]

    first_move = str(chess_files[first_square[0]]) + str(chess_ranks[first_square[1]])
    second_move = str(chess_files[second_square[0]]) + str(chess_ranks[second_square[1]])

    return first_move, second_move

def draw_Board(screen):
    colors = [p.Color("white"), p.Color("gray")]

    for r in range(DIMENSION):
        for c in range(DIMENSION):
           color = colors[ ( (r+c)%2 )] 
           p.draw.rect(screen,color, p.Rect(c*Square_Size, r*Square_Size, Square_Size, Square_Size))

def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if (piece != "--"):
                if( piece[0] == "b"):   
                    screen.blit(IMAGES[piece], p.Rect(col*Square_Size, row*Square_Size, Square_Size, Square_Size))


def draw_software_board(move):

    first_move, second_move = map_move(move)
    gs.board[int(second_move[1])][int(second_move[0])] = gs.board[int(first_move[1])][int(first_move[0])]
    gs.board[int(first_move[1])][int(first_move[0])] = "--"

    running4 = True
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    while(running4):
        
        # print("hello")

        for event in p.event.get():
            if event.type == p.QUIT:
                pygame.quit()
                running4 = False
       
        if(running4):
            # cam.takePicture()
            draw_Board(screen)
            draw_pieces(screen,gs.board)
            clock.tick(MAX_FPS)
            p.display.flip()

def load_Images():

    list_Pieces = ['wp','wR','wN','wB','wQ','wK','bp','bR','bN','bB','bQ','bK']
    for piece in list_Pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("pieceImages/"+piece+".png"), ( Square_Size ,Square_Size))

load_Images()
screen = p.display.set_mode((WIDTH,HEIGHT))
#Take picture by pressing s, press q to quit
# cam.takePicture()

#TAKING EMPTY BOARD PICTURE
running = True
while(running):
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            running = False

    if(running):
        draw_Board(screen)
        clock.tick(MAX_FPS)
        p.display.flip()
        cam.boardPicture()


# cam.boardPicture()

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
#
# cv2.imshow("Board", board)
# cv2.waitKey(0)

#TAKING INITIAL BOARD STATE PICTURE
print("Take a picture of the initial board setup.")
running2 = True
p.init()
screen = p.display.set_mode((WIDTH,HEIGHT))
while(running2):
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            running2 = False

    if(running2):
        draw_Board(screen)
        # draw_pieces(screen,gs.board)
        clock.tick(MAX_FPS)
        p.display.flip()
        cam.movePicture(0)
    


previous = cv2.imread("images\mygame\move0.jpg")
previous = Processing.processImage(previous)
previous = Processing.findEdges(previous)[0]

c=1
while(True):
    #HARDWARE MOVE
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    running3 = True
    while (running3):
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                running3 = False
        
        if(running3):
            while(True):
                draw_Board(screen)
                clock.tick(MAX_FPS)
                p.display.flip()
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
        ucimove = chess.Move.from_uci(userMove)
        if (ucimove not in engboard.legal_moves): 
            print("Move is not valid.")
        else:
            break

    if (engboard.is_capture(ucimove) or engboard.is_en_passant(ucimove)):
        print("Black has captured a piece on " + userMove[2:] + ". Please take a picture of the current state.")
        cam.movePicture(c)
        current = cv2.imread("images\mygame\move{}.jpg".format(c))
        current = Processing.processImage(current)
        current = Processing.findEdges(current)[0]

    if (engboard.is_checkmate() == True):
        print("Checkmate! Black Wins!")
        break
    if (engboard.is_stalemate() == True):
        print("Stalemate!")
        break
    engboard.push_san(userMove)
    draw_software_board(userMove)
    print(engboard)

    previous = current
    c += 1




