import numpy as np
from collections import namedtuple

Position = namedtuple('Position', ['row','col'])

class Tetramino(object):
    "Tetramino object subclasses all the tetraminos"
    PIECE_GRID_ROWS = 1
    PIECE_GRID_COLS = 1
    PIECE_ORIENTATIONS = 1

    def __init__(self, position=Position(0,0)):
        # position is the upper left corner of the tetramino in the grid
        self.position = position
        self.orientation = 0
        # orientations_grid[orientation][row][column]
        self.orientations_grid = np.empty((self.PIECE_ORIENTATIONS,\
                                           self.PIECE_GRID_ROWS,\
                                           self.PIECE_GRID_COLS), dtype=str)
        self.orientations_grid[:,:,:] = '.'
        self.piece_grid = self.orientations_grid[0,:,:]

    def display_piece_grid(self):
        for row in range(self.PIECE_GRID_ROWS):
            print ' '.join(self.piece_grid[row])

    def test_tetramino(self):
        self.display_piece_grid()

    # rotate method is in Tetramino, NOT in model, because it modifies
    # the Tetramino itself (and not the main grid)
    def rotate_right(self):
        if self.orientation < self.PIECE_ORIENTATIONS-1:
            self.orientation += 1
        else:
            self.orientation = 0
        self.piece_grid = self.orientations_grid[self.orientation,:,:]
        return self

class I_Tetramino(Tetramino):
    """ Implementation of the I Tetramino
    orientation: 0 = horizontal, 1 = vertical """
    PIECE_GRID_ROWS = 4
    PIECE_GRID_COLS = 4
    PIECE_ORIENTATIONS = 4

    def __init__(self, position=Position(0,3)):
        Tetramino.__init__(self, position)
        # orientations
        self.orientations_grid[0,1,:] = ['c','c','c','c']
        self.orientations_grid[1,:,2] = ['c','c','c','c']
        self.orientations_grid[2,2,:] = ['c','c','c','c']
        self.orientations_grid[3,:,1] = ['c','c','c','c']
        self.piece_grid = self.orientations_grid[0,:,:]

class O_Tetramino(Tetramino):
    """ Implementation of the O Tetramino """
    PIECE_GRID_ROWS = 2
    PIECE_GRID_COLS = 2
    PIECE_ORIENTATIONS = 1

    def __init__(self, position=Position(0,4)):
        Tetramino.__init__(self, position)
        # orientation 0: 2x2 square 'y'
        self.orientations_grid[0,:,:] = [['y','y'],['y','y']]
        self.piece_grid = self.orientations_grid[0,:,:]

class Z_Tetramino(Tetramino):
    """ Implementation of the Z Tetramino """
    PIECE_GRID_ROWS = 3
    PIECE_GRID_COLS = 3
    PIECE_ORIENTATIONS = 4

    def __init__(self, position=Position(0,3)):
        Tetramino.__init__(self, position)
        # orientations
        self.orientations_grid[0,:,:] = [['r','r','.'],['.','r','r'],['.','.','.']]
        self.orientations_grid[1,:,:] = [['.','.','r'],['.','r','r'],['.','r','.']]
        self.orientations_grid[2,:,:] = [['.','.','.'],['r','r','.'],['.','r','r']]
        self.orientations_grid[3,:,:] = [['.','r','.'],['r','r','.'],['r','.','.']]
        self.piece_grid = self.orientations_grid[0,:,:]

class S_Tetramino(Tetramino):
    """ Implementation of the S Tetramino """
    PIECE_GRID_ROWS = 3
    PIECE_GRID_COLS = 3
    PIECE_ORIENTATIONS = 4

    def __init__(self, position=Position(0,3)):
        Tetramino.__init__(self, position)
        # orientations
        self.orientations_grid[0,:,:] = [['.','g','g'],['g','g','.'],['.','.','.']]
        self.orientations_grid[1,:,:] = [['.','g','.'],['.','g','g'],['.','.','g']]
        self.orientations_grid[2,:,:] = [['.','.','.'],['.','g','g'],['g','g','.']]
        self.orientations_grid[3,:,:] = [['g','.','.'],['g','g','.'],['.','g','.']]
        self.piece_grid = self.orientations_grid[0,:,:]

class J_Tetramino(Tetramino):
    """ Implementation of the J Tetramino """
    PIECE_GRID_ROWS = 3
    PIECE_GRID_COLS = 3
    PIECE_ORIENTATIONS = 4

    def __init__(self, position=Position(0,3)):
        Tetramino.__init__(self, position)
        # orientation 0
        self.orientations_grid[0,:,:] = [['b','.','.'],['b','b','b'],['.','.','.']]
        self.orientations_grid[1,:,:] = [['.','b','b'],['.','b','.'],['.','b','.']]
        self.orientations_grid[2,:,:] = [['.','.','.'],['b','b','b'],['.','.','b']]
        self.orientations_grid[3,:,:] = [['.','b','.'],['.','b','.'],['b','b','.']]
        self.piece_grid = self.orientations_grid[0,:,:]

class L_Tetramino(Tetramino):
    """ Implementation of the J Tetramino """
    PIECE_GRID_ROWS = 3
    PIECE_GRID_COLS = 3
    PIECE_ORIENTATIONS = 4

    def __init__(self, position=Position(0,3)):
        Tetramino.__init__(self, position)
        # orientation 0
        self.orientations_grid[0,:,:] = [['.','.','o'],['o','o','o'],['.','.','.']]
        self.orientations_grid[1,:,:] = [['.','o','.'],['.','o','.'],['.','o','o']]
        self.orientations_grid[2,:,:] = [['.','.','.'],['o','o','o'],['o','.','.']]
        self.orientations_grid[3,:,:] = [['o','o','.'],['.','o','.'],['.','o','.']]
        self.piece_grid = self.orientations_grid[0,:,:]

class T_Tetramino(Tetramino):
    """ Implementation of the J Tetramino """
    PIECE_GRID_ROWS = 3
    PIECE_GRID_COLS = 3
    PIECE_ORIENTATIONS = 4

    def __init__(self, position=Position(0,3)):
        Tetramino.__init__(self, position)
        # orientation 0
        self.orientations_grid[0,:,:] = [['.','m','.'],['m','m','m'],['.','.','.']]
        self.orientations_grid[1,:,:] = [['.','m','.'],['.','m','m'],['.','m','.']]
        self.orientations_grid[2,:,:] = [['.','.','.'],['m','m','m'],['.','m','.']]
        self.orientations_grid[3,:,:] = [['.','m','.'],['m','m','.'],['.','m','.']]
        self.piece_grid = self.orientations_grid[0,:,:]
