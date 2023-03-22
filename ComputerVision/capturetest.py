import chess

#CREATING ENGINE BOARD
engboard = chess.Board()

while(True):
    #WHITE MOVE
    while(True):
        userMove = input("Enter the white move: ")
        ucimove = chess.Move.from_uci(userMove)
        if (ucimove not in engboard.legal_moves):
            print("Move is not valid.")
        else:
            break

    if (engboard.is_capture(ucimove)):
        print("takes")
    engboard.push_san(userMove)
    print(engboard)

    if (engboard.is_checkmate() == True):
        print("Checkmate! White Wins!")
        break

    if (engboard.is_stalemate() == True):
        print("Stalemate!")
        break

    #BLACK WHITE MOVE
    while (True):
        userMove = input("Enter the black move: ")
        ucimove = chess.Move.from_uci(userMove)
        if (ucimove not in engboard.legal_moves):
            print("Move is not valid.")
        else:
            break

    if (engboard.is_capture(ucimove)):
        print("takes")
    engboard.push_san(userMove)
    print(engboard)

    if (engboard.is_checkmate() == True):
        print("Checkmate! Black Wins!")
        break

    if (engboard.is_stalemate() == True):
        print("Stalemate!")
        break

