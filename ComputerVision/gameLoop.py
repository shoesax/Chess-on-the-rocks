import cv2
import Camera
import Processing
import Movement

import ChessEngine as engine
import pygame as p
import time

WIDTH = HEIGHT = 800
DIMENSION = 8
Square_Size = HEIGHT // DIMENSION
Max_FPS = 15
IMAGES = {}
rank = {"a":1, "b":2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h":8}
# screen = p.display.set_mode((WIDTH,HEIGHT))
# time.sleep(1)
# p.quit()
# time.sleep(1)
# gs = engine.GameState()



game_over = False

def teardown_board():
    p.quit()

def load_Images():
    
    list_Pieces = ['wp','wR','wN','wB','wQ','wK','bp','bR','bN','bB','bQ','bK']
    for piece in list_Pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("pieceImages/"+piece+".png"), (Square_Size,Square_Size))

def ask_user_for_input():

    starting_square = input("Enter square you want to move from: \n ")
    ending_square = input("Enter square you want to move to: \n")

    return starting_square, ending_square

def board_init():

    print("board init")

def hardware_move():
    print("hardware move")

def software_move():
    running = True
    sq_selected = ()
    player_clicks = [] #will contain two sqSelected

    while(running):
        for e in p.event.get():
            if e.type == e.QUIT():
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // Square_Size
                row = location[1] // Square_Size
                sq_selected = (row, col)
                player_clicks.append(sq_selected)

                if len(player_clicks) == 2:
                    move = engine.Move(player_clicks[0], player_clicks[1], gs.board)
                    sq_selected = ()
    print("software move")


def take_picture():
    print("take picture")

def draw_game_state(screen,gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)

def draw_board(screen):
    colors = [p.Color("white"), p.Color("dark green")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
           color = colors[ ( (r+c)%2 )] 
           p.draw.rect(screen,color, p.Rect(c*Square_Size, r*Square_Size, Square_Size, Square_Size) )

def draw_pieces(screen,board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(col*Square_Size, row*Square_Size, Square_Size, Square_Size))

def update_Board(square_One, square_Two, gs):

    # board = gs.board
    print_board(gs.board)
    gs.board[(rank[str(square_Two[0])])][int(square_Two[1])] = gs.board[(rank[str(square_One[0])])][int(square_One[1])] 
    print(gs.board[(rank[str(square_Two[0])])][int(square_Two[1])])
    gs.board[(rank[str(square_One[0])])][int(square_One[1])] = "--"
    print_board(gs.board)

def print_board(board):
    for i in board:
        print(i)

def software_move_beta(sq_one, sq_two, board):
    pass
    
# board_init()
# load_Images()

def main():

    gs = engine.GameState()
    sq_one = input("enter starting square: ")
    sq_two = input("enter ending square: ")
    mov = engine.Move(sq_one, sq_two, gs.board)
    print_board(gs.board)












if __name__ == "__main__":
    main()
