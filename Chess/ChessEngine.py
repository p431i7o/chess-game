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
            ["--", "--", "--", "bp", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.moveFunctions = {'p':self.get_pawn_moves,'R':self.get_rook_moves,'N':self.get_knight_moves,
                              'B':self.get_bishop_moves,'Q':self.get_queen_moves,'K':self.get_king_moves}
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

    '''
    All moves considering checks
    '''
    def get_valid_moves(self):
        return self.get_all_possible_moves() #for now we will not worry about checks

    '''
    All moves without considering checks
    '''
    def get_all_possible_moves(self):
        moves = [Move((6,4),(4,4),self.board)]
        for row in range(len(self.board)): #number of rows
            for col in range(len(self.board[row])): #number of cols in a given row
                turn = self.board[row][col][0] #w or b, it could be also called color
                if (turn=='w' and self.whiteToMove) or (turn=='b' and not self.whiteToMove):
                    piece = self.board[row][col][1]
                    self.moveFunctions[piece](row, col, moves)#calls the appropiate move function based on the piece type
        return moves

    '''
    Get all the pawn moves for the pawn located at row, col and add these moves to the list
    '''
    def get_pawn_moves(self, row, col, moves):
        if self.whiteToMove:
            if self.board[row-1][col] == "--": #1 square pawn advance
                moves.append(Move((row,col),(row-1,col),self.board))
                if row == 6 and self.board[row-2][col] == "--": #2 square pawn advance
                    moves.append(Move((row,col),(row-2,col),self.board))
            if col-1 >=0:#captures to the lef
                if self.board[row-1][col-1][0]=="b":#enemy piece to capture
                    moves.append(Move((row,col),(row-1,col-1),self.board))
            if col+1<=7:#Captures to the right
                if self.board[row-1][col+1][0]=="b":#enemy piece to capture
                    moves.append(Move((row,col),(row-1,col+1),self.board))


    '''
    Get all the rook moves for the rook located at row, col and add these moves to the list
    '''
    def get_rook_moves(self, row, col, moves):
        pass

    def get_knight_moves(self, row, col,moves):
        pass

    def get_bishop_moves(self, row, col, moves):
        pass

    def get_queen_moves(self, row, col, moves):
        pass

    def get_king_moves(self, row, col, moves):
        pass


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
        self.moveID = self.start_row*1000 + self.start_col*100 + self.end_row*10 + self.end_col
        print(self.moveID)
    '''
    Overriding the equal method
    '''
    def __eq__(self, other):
        if isinstance(other,Move):
            return self.moveID == other.moveID
        return False

    def get_chess_notation(self):
        #You can add to make more like real chess notation
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, row, col):
        return self.cols_to_files[col] + self.rows_to_ranks[row]