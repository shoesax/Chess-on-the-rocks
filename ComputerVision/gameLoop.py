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
gs = engine.GameState()



game_over = False

def ask_user_for_input():

    starting_square = input("Enter square you want to move from: \n ")
    ending_square = input("Enter square you want to move to: \n")

    return starting_square, ending_square

def board_init():

    print("board init")

def hardware_move():
    print("hardware move")

def software_move(square_one, square_two):
    print("software move")

def take_picture():
    print("take picture")
    
board_init()

while(not game_over):

    starting_square, ending_square = ask_user_for_input()
    print(starting_square, ending_square)
    break


