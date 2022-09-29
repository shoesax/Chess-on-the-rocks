import pygame as p
import ChessEngine as engine 


p.init()
WIDTH = HEIGHT = 400
DIMENSION = 8
Square_Size = HEIGHT // DIMENSION

Max_FPS = 15
Images = {}


''' TO DO: ADD IMAGES TO THE REPO SO THIS FUNCTION CAN BE CALLED. WILL THROW  UP AN ERROR IF CALLED IN CURRENT STATE '''
def load_Images():

    list_Pieces = ['wp','wR','wN','wB','wQ','wK','bp','bR','bN','bB','bQ','bK']
    for piece in list_Pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/"+piece+".png"), (Square_size,Square_Size))


def main():
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()

    gs = engine.GameState()
    load_Images()


