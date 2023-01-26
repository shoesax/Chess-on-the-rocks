import chess
#import chess.uci  isn't supported anymore, use chess.engine instead  https://github.com/niklasf/python-chess/discussions/848
import numpy as np
import stockfish
from Board import Board
import chess.engine


class ChessEng:
    '''
    This class interacts with the stockfish chess engine using the python-chess
    package. All interactions are done with the Universal Chess Interface protocol (UCI)
    Transcribes game to a txt file called Game.txt
    '''

    def __init__(self):
        '''
        Creates chessboard, local chess engine stockfish, and initiates UCI protocol
        '''

        self.engBoard = chess.Board()
        self.engine = chess.chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish") #change directory
        self.engine.engine()
        print(self.engBoard)

    def updateMove(self, move):
        '''
        Updates chess board with the move made. Also checks for illegal moves
        '''

        # convert move to UCI format for engine
        uciMove = chess.Move.from_uci(move)

        # check legality
        if uciMove not in self.engBoard.legal_moves:
            return 1
        else:
            # update board
            self.engBoard.push(uciMove)
            print(self.engBoard)
            return 0

#Not necessry as user is making a move themselves, need to create user input function that also writes to a txt file
    # def feedToAI(self):
    #     '''
    #     Gets the bestmove from the stockfish engine. Writes move choice to Game.txt file
    #     '''
    #
    #     # giving the CPU the current board position
    #     self.engine.position(self.engBoard)
    #
    #     # Giving the engine 2000ms to produce a move
    #     response = self.engine.go(movetime=2000)
    #     bestMove = response[0]
    #
    #     # update board
    #     self.engBoard.push(bestMove)
    #
    #     # write move to txt file
    #     f = open("Game.txt", "a+")
    #     f.write(bestMove.uci() + "\r\n")
    #     f.close()
    #
    #     print(self.engBoard)
    #     return bestMove

