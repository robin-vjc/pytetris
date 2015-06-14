__author__ = 'Robin'
"""
Graphical interface for pyTetris
"""

import pygame, sys
from pygame.locals import *
from tetris import *
from collections import namedtuple

Color = namedtuple("Color", ['red', 'green', 'blue'])
cyan = Color(0,200,200)
green = Color(0,200,0)
red = Color(200,0,0)
blue = Color(0,0,255)
darkBlue = Color(0,0,128)
white = Color(255,255,255)
black = Color(0,0,0)
pink = Color(255,200,200)

# Instantiate pyTetris engine
model = Model()
viewer = Viewer(model)
controller = Controller(model, viewer)

# pygame setup
# ------------
WIDTH = 240
HEIGHT = 480
DX = 20
DY = 20
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(black)

# Setup background grid
# ---------------------
for col in range(model.GRID_COLS+1):
    line_color = white
    pygame.draw.line(screen, line_color, (DX*(col+1), DY), (DX*(col+1), HEIGHT-DY), (1))

for row in range(model.GRID_ROWS+1):
    if row == 2:
        line_color = red
    else:
        line_color = white
    pygame.draw.line(screen, line_color, (DX, DY*(row+1)), (WIDTH-DX, DY*(row+1)), (1))


clock = pygame.time.Clock()

def place_block(position, color):
    # TODO implement
    """ Draws a rectangle of the given color in the grid
    :param position: Position in the grid where the block should be placed
    :param color: Color of the block
    :return: None
    """
    pass

def draw_grid():
    # TODO draws all the blocks
    # read from model settled blocks and merged

while 1:
    clock.tick(60)
    # EVERY 60-5*level PRESS V

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        DX+=20
        DY+=20
    #pygame.draw.line(screen, (0, 200, 200), (20, y), (580, x), (1))
    #pygame.draw.line(screen, (0, 200, 200), (x, 20), (x, 380), (1))