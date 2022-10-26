import pygame as p
import ChessEngine as engine 
position = 'A1'


p.init()
WIDTH = HEIGHT = 800
DIMENSION = 8
Square_Size = HEIGHT // DIMENSION
Max_FPS = 15
IMAGES = {}


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
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  #Location of mouse
                # location = p.mouse.get.pos()
                col = location[0] // Square_Size
                row = location[1] // Square_Size
                print("hello")
                poisiton = input("Enter position: ")

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

if __name__ == "__main__":
    main()



