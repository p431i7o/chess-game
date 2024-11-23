"""
This class is responsible for:
 - Storing all the information about the current state of a chess game.
 - Also will be responsible for determining the valid moves at the current state.
 - It will also keep a move log.
"""
class GameState:
    def __init__(self):
        #board is an 8x8 2d list
        #each element of the list has 2 characters
        #the first character represent the color of the piece 'b' or 'w'
        #the second character represent the type of the piece 'Q', 'K', 'R', 'B','N' or 'P'
        #'--' represents an empty space with no piece
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.whiteToMove = True
        self.moveLog = []