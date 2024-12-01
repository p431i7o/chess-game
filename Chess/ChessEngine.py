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

    '''
    Takes a move as a parameter and executes (this will not work for castling, pawn promotion and en-peasant)
    '''
    def make_move(self, move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.moveLog.append(move) #log the move so we can undo it later
        self.whiteToMove = not self.whiteToMove #we swap players

    '''
    Undo the last move made
    '''
    def undo_move(self):
        if len(self.moveLog) != 0: #make sure that there is a move to undo
            move = self.moveLog.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.whiteToMove = not self.whiteToMove #switch turns back

class Move():
    # maps  keys to values
    # key: value
    ranks_to_rows= { "1":7, "2":6, "3":5, "4":4, "5":3, "6":2, "7":1, "8":0,}
    rows_to_ranks = {v:k for k,v in ranks_to_rows.items()}

    files_to_cols = { "a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7,}
    cols_to_files = {v:k for k,v in files_to_cols.items()}

    def __init__(self, start_square, end_square, board):
        self.start_row = start_square[0]
        self.start_col = start_square[1]
        self.end_row = end_square[0]
        self.end_col = end_square[1]

        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]

    def get_chess_notation(self):
        #You can add to make more like real chess notation
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, row, col):
        return self.cols_to_files[col] + self.rows_to_ranks[row]