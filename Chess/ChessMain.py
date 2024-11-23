"""
This is our main driver file. It will be responsible for:
 - handling user input
 - displaying the current GameState object.
"""

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512  #400 is another good option
DIMENSION = 8  #dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  #for animations later on
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called exactly once in the main
'''


def load_images():
    pieces = ['wp', 'bp', 'wR', 'bR', 'wQ', 'bQ', 'bK', 'wK', 'wB', 'bB', 'wN', 'bN']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))
    #Note: we can access an image by saying IMAGES['wp']


'''
The main driver for our code. This will handle user input and updating the graphics
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))

    gs = ChessEngine.GameState()
    load_images()  # Only do this once before the while loop
    running = True
    sq_selected = ()  #no square is selected, keep track of the last click of the user (tuple: row,col)
    player_clicks = [] #keep track of a player clicks (two tuples: [(6,4), (4,4)])
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            elif event.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  #(x,y)
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sq_selected == (row, col): #the user clicked the same square twice
                    sq_selected = () #deselect
                    player_clicks = [] #clear the player clicks
                else:
                    sq_selected = (row, col)
                    player_clicks.append(sq_selected) #append for both 1st and 2nd clicks
                if len(player_clicks) == 2: #After the second click
                    move = ChessEngine.Move(player_clicks[0], player_clicks[1], gs.board)
                    print(move.get_chess_notation())
                    gs.make_move(move)
                    sq_selected = () #reset user clicks
                    player_clicks = []

        draw_game_state(screen, gs)

        clock.tick(MAX_FPS)
        p.display.flip()


def draw_game_state(screen, game_state):
    draw_board(screen)  #Draw squares on the board
    #add in piece highlighting or move suggestions (later)
    draw_pieces(screen, game_state.board)  #Draw the pieces on top of the squares


'''
Draw the squares on the board.
Always the top left square is light
'''


def draw_board(screen):
    colors = [p.Color('light gray'), p.Color('dark green')]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col) % 2)]
            p.draw.rect(screen, color, p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Draw the pieces on the board using the current GameState.board
'''


def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":  #not an empty space
                screen.blit(IMAGES[piece], (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == '__main__':
    main()
