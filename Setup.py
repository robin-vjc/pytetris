__author__ = 'Robin'
""" Settings file, for the GUI of pyTetris """

import pygame, sys
from pygame.locals import *
from tetris import *
from collections import namedtuple

# Instantiate pyTetris engine
# ---------------------------
model = Model()
viewer = Viewer(model)
controller = Controller(model, viewer)
pygame.init()

# Colors
# ------
Color = namedtuple("Color", ['red', 'green', 'blue'])

CYAN = Color(0,200,200)
GREEN = Color(0,200,0)
RED = Color(200,0,0)
BLUE = Color(0,0,255)
DARKBLUE = Color(0,0,128)
WHITE = Color(255,255,255)
BLACK = Color(0,0,0)
MAGENTA = Color(255,200,200)
YELLOW = Color(255,255,0)
ORANGE = Color(255,165,0)

# pygame setup
# ------------
# display size
DX = 20
DY = 20
WIDTH = int((model.GRID_COLS+2)*DX)
HEIGHT = int((model.GRID_ROWS+2)*DX)
# refresh rate
RATE = 30


TETRAMINOS = ('I','J','L','O','T','Z','S')
COLORCODE = {
    'c': CYAN,
    'C': CYAN,
    'y': YELLOW,
    'Y': YELLOW,
    'r': RED,
    'R': RED,
    'g': GREEN,
    'G': GREEN,
    'b': BLUE,
    'B': BLUE,
    'o': ORANGE,
    'O': ORANGE,
    'm': MAGENTA,
    'M': MAGENTA,
    '.': BLACK
}

screen = pygame.display.set_mode((WIDTH,HEIGHT))
myfont = pygame.font.SysFont("monospace", 15)

# Helper functions
# ----------------
def draw_block(position, color):
    """ Draws a rectangle of the given color in the grid
    :param position: Position in the grid where the block should be placed
    :param color: Color of the block
    :return: None
    """
    x = position.col*DX+DX+2
    y = position.row*DY+DY+2
    width = DX-4
    height = DY-4
    pygame.draw.rect(screen, color, (x,y,width,height), 0)

def draw_grid():
    screen.fill(BLACK)
    # Setup background grid
    for col in range(model.GRID_COLS+1):
        line_color = WHITE
        pygame.draw.line(screen, line_color, (DX*(col+1), DY), (DX*(col+1), HEIGHT-DY), (1))
    for row in range(model.GRID_ROWS+1):
        if row == 2:
            line_color = RED
        else:
            line_color = WHITE
        pygame.draw.line(screen, line_color, (DX, DY*(row+1)), (WIDTH-DX, DY*(row+1)), (1))
    # draw filled blocks
    for row in range(model.GRID_ROWS):
        for col in range(model.GRID_COLS):
            if model.grid[row,col] != '.':
                draw_block(Position(row,col), COLORCODE[model.grid[row,col]])
            if model.active_grid[row,col] != '.':
                draw_block(Position(row,col), COLORCODE[model.active_grid[row,col]])
    # draw score
    draw_score(model.score, model.level)
    # refresh console, for debugging
    controller.exec_command('p')

def draw_score(score, level):
    text = myfont.render("".join(["Score: ", str(score), " Level: ", str(level)]),
                         1, (255,255,255))
    screen.blit(text, (1, 1))
