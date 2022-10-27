# from curses import KEY_DOWN
from asyncio.windows_events import NULL
import pygame as p
import ChessEngine as engine 

p.init()
WIDTH = HEIGHT = 800
DIMENSION = 8
Square_Size = HEIGHT // DIMENSION
Max_FPS = 15
IMAGES = {}
rank = {"a":1, "b":2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h":8}


''' TO DO: ADD IMAGES TO THE REPO SO THIS FUNCTION CAN BE CALLED. WILL THROW  UP AN ERROR IF CALLED IN CURRENT STATE '''
def load_Images():
    
    list_Pieces = ['wp','wR','wN','wB','wQ','wK','bp','bR','bN','bB','bQ','bK']
    for piece in list_Pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/images/"+piece+".png"), (Square_Size,Square_Size))


def main():
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()

    gs = engine.GameState()
    load_Images() 

    square_selected= () #No square is selected originally. Keeps track of users last click. Replace with arduino input code

    running = True
    user_text = ""
    char_count = 0
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.KEYDOWN:
                if char_count < 4:
                    user_text += e.unicode
                    char_count += 1
                else:
                    char_count = 0
                    square_to_move = user_text[0:2]
                    square_to_move_to = user_text[2:4] 

                    update_Board(square_to_move, square_to_move_to, gs.board)

                    square_to_move = ""
                    square_to_move_to = ""
        


        draw_Game_State(screen, gs)
        clock.tick(Max_FPS)
        p.display.flip()
        

def draw_Game_State(screen, gs):
    draw_Board(screen)
    draw_Pieces(screen,gs.board)

def draw_Board(screen):
    colors = [p.Color("white"), p.Color("dark green")]

    for r in range(DIMENSION):
        for c in range(DIMENSION):
           color = colors[ ( (r+c)%2 )] 
           p.draw.rect(screen,color, p.Rect(c*Square_Size, r*Square_Size, Square_Size, Square_Size) )

def draw_Pieces(screen,board):

    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(col*Square_Size, row*Square_Size, Square_Size, Square_Size))

def update_Board(square_One, square_Two, board):

    board[(rank[str(square_Two[0])])][int(square_Two[1])] = board[(rank[str(square_One[0])])][int(square_One[1])] 
    board[(rank[str(square_One[0])])][int(square_One[1])] = "--"
    

if __name__ == "__main__":
    main()



