import cv2
import Camera
import Processing
import Movement

import ChessEngine as engine
import pygame as p
import time

MAX_FPS = 15

gs = engine.GameState()

main_loop = True

chess_files = { "a":0, "b": 1, "c": 2,"d": 3, "e": 4, "f":5, "g": 6, "h": 7}
chess_ranks = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7}

DIMENSION = 8
HEIGHT = 800
WIDTH = HEIGHT
Square_Size = HEIGHT // DIMENSION

IMAGES = {}

def print_board(board):
    for i in board:
        print(i)

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

def draw_pieces(screen,board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(col*Square_Size, row*Square_Size, Square_Size, Square_Size))

def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if (piece != "--"):
                if( piece[0] == "b"):   
                    screen.blit(IMAGES[piece], p.Rect(col*Square_Size, row*Square_Size, Square_Size, Square_Size))

def load_Images():

    list_Pieces = ['wp','wR','wN','wB','wQ','wK','bp','bR','bN','bB','bQ','bK']
    for piece in list_Pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("pieceImages/"+piece+".png"), ( Square_Size ,Square_Size))

load_Images()


while(main_loop):

    software_move = True
    #Look for software move
    while(software_move):
        user_move = input("Enter the PC user move: ")
        first_move, second_move = map_move(user_move)
        gs.board[int(second_move[1])][int(second_move[0])] = gs.board[int(first_move[1])][int(first_move[0])]
        gs.board[int(first_move[1])][int(first_move[0])] = "--"
        print_board(gs.board)
                                    
        software_move = False

    running = True
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    while(running):
        
        # print("hello")

        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                running = False

        # screen = p.display.set_mode((WIDTH,HEIGHT))
        # draw_Board(screen)
       
        if(running):
            draw_Board(screen)
            draw_pieces(screen,gs.board)
            clock.tick(MAX_FPS)
            p.display.flip()

    