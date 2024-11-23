"""
This is our main driver file. It will be responsible for:
 - handling user input
 - displaying the current GameState object.
"""

import pygame as p
from Chess import ChessEngine
WIDTH = HEIGHT = 512 #400 is another good option
DIMENSION = 8 #dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #for animations later on
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called exactly once in the main
'''
def loadImages():
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
    loadImages()# Only do this once before the while loop
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        drawGameState(screen, gs)

        clock.tick(MAX_FPS)
        p.display.flip()

def drawGameState(screen, gameState):
    drawBoard(screen) #Draw squares on the board
    #add in piece highlighting or move suggestions (later)
    drawPieces(screen, gameState.board) #Draw the pieces on top of the squares

'''
Draw the squares on the board.
Always the top left square is light
'''
def drawBoard(screen):
    colors = [p.Color('light gray'), p.Color('dark green')]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row+col)%2)]
            p.draw.rect(screen, color, p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))
'''
Draw the pieces on the board using the current GameState.board
'''
def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--": #not a empty space
                screen.blit(IMAGES[piece], (col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == '__main__':
    main()