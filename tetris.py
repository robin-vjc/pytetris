import numpy as np
from collections import namedtuple

Position = namedtuple('Position', ['row','column'])
Block = namedtuple('Block', ['row', 'column', 'color'])

class Tetramino(object):
    "Tetramino object subclasses all the tetraminos"
    PIECE_GRID_ROWS = 1
    PIECE_GRID_COLS = 1
    PIECE_ORIENTATIONS = 1

    def __init__(self, position=Position(0,0)):
        self.position = position
        self.orientation = 0
        # orientations_grid[orientation][row][column]
        self.orientations_grid = np.empty((self.PIECE_ORIENTATIONS,\
                                           self.PIECE_GRID_ROWS,\
                                           self.PIECE_GRID_COLS), dtype=object)
        self.orientations_grid[:,:,:] = '.'
        self.piece_grid = self.orientations_grid[0,:,:]

    def display_piece_grid(self):
        for row in range(self.PIECE_GRID_ROWS):
            print ' '.join(self.piece_grid[row])

    def test_tetramino(self):
        self.display_piece_grid()

    def rotate_right(self):
        if self.orientation < self.PIECE_ORIENTATIONS-1:
            self.orientation += 1
        else:
            self.orientation = 0
        self.piece_grid = self.orientations_grid[self.orientation,:,:]
        # return self.piece_grid

class I_Tetramino(Tetramino):
    """ Implementation of the I Tetramino
    orientation: 0 = horizontal, 1 = vertical """
    PIECE_GRID_ROWS = 4
    PIECE_GRID_COLS = 4
    PIECE_ORIENTATIONS = 4

    def __init__(self, position=Position(0,0)):
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

    def __init__(self, position=Position(0,0)):
        Tetramino.__init__(self, position)
        # orientation 0: 2x2 square 'y'
        self.orientations_grid[0,:,:] = [['y','y'],['y','y']]
        self.piece_grid = self.orientations_grid[0,:,:]

class Z_Tetramino(Tetramino):
    """ Implementation of the Z Tetramino """
    PIECE_GRID_ROWS = 3
    PIECE_GRID_COLS = 3
    PIECE_ORIENTATIONS = 4

    def __init__(self, position=Position(0,0)):
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

    def __init__(self, position=Position(0,0)):
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

    def __init__(self, position=Position(0,0)):
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

    def __init__(self, position=Position(0,0)):
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

    def __init__(self, position=Position(0,0)):
        Tetramino.__init__(self, position)
        # orientation 0
        self.orientations_grid[0,:,:] = [['.','m','.'],['m','m','m'],['.','.','.']]
        self.orientations_grid[1,:,:] = [['.','m','.'],['.','m','m'],['.','m','.']]
        self.orientations_grid[2,:,:] = [['.','.','.'],['m','m','m'],['.','m','.']]
        self.orientations_grid[3,:,:] = [['.','m','.'],['m','m','.'],['.','m','.']]
        self.piece_grid = self.orientations_grid[0,:,:]


class Model(object):
    "model stores grid state, pieces and their position"
    gridRows = 22
    gridColumns = 10

    def __init__(self):
        self.grid = [['.']*self.gridColumns for x in range(self.gridRows)]
        self.tetraminos = []
        self.active_tetramino = Tetramino()
        self.score = 0
        self.cleared_lines = 0
        self._observers = []

    def add_tetramino(self, tetramino):
        self.tetraminos.append(tetramino)
        self.active_tetramino = tetramino

    def rotate_right(self):
        self.active_tetramino.rotate_right()

    def test_tetramino(self):
        self.active_tetramino.test_tetramino()

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

class Viewer(object):
    "is an observer to the model"

    def __init__(self, model):
        self.model = model
        self.model.add_observer(self)

    def display_grid(self):
        for row in range(self.model.gridRows):
            print ' '.join(self.model.grid[row])

    def display_score(self):
        print self.model.score

    def display_cleared_lines(self):
        print self.model.cleared_lines

    def update(self, model):
        "what to do when model is updated"
        self.display_grid()

class Controller(object):

    def given_grid(self):
        temp_grid = self.model.grid
        for i in range(self.model.gridRows):
            input_row = raw_input('')
            temp_grid[i][:] = input_row.split(' ')
        self.model.grid = temp_grid

    def clear_grid(self):
        self.model.grid = [['.']*self.model.gridColumns for x in range(self.model.gridRows)]

    def step(self):
        # if row is complete, erase it
        for i, row in enumerate(self.model.grid):
            if '.' not in row:
                self.model.grid[i][:] = ['.']*self.model.gridColumns
                self.model.cleared_lines += 1
                self.model.score += 100

    def print_empty_line(self):
        print ''


    def __init__(self, model, viewer):
        self.model = model
        self.viewer = viewer

        self.options = {'q': quit,
                        'p': self.viewer.display_grid,
                        'g': self.given_grid,
                        'c': self.clear_grid,
                        's': self.step,
                        '?s': self.viewer.display_score,
                        '?n': self.viewer.display_cleared_lines,
                        'I': self.model.add_tetramino,
                        'J': self.model.add_tetramino,
                        'L': self.model.add_tetramino,
                        'O': self.model.add_tetramino,
                        'S': self.model.add_tetramino,
                        'T': self.model.add_tetramino,
                        'Z': self.model.add_tetramino,
                        ')': self.model.rotate_right,
                        't': self.model.test_tetramino,
                        ';': self.print_empty_line}

    def exec_command(self, keystroke):
        if keystroke == 'I':
            self.options[keystroke](I_Tetramino())
        elif keystroke == 'J':
            self.options[keystroke](J_Tetramino())
        elif keystroke == 'L':
            self.options[keystroke](L_Tetramino())
        elif keystroke == 'O':
            self.options[keystroke](O_Tetramino())
        elif keystroke == 'T':
            self.options[keystroke](T_Tetramino())
        elif keystroke == 'Z':
            self.options[keystroke](Z_Tetramino())
        elif keystroke == 'S':
            self.options[keystroke](S_Tetramino())
        else:
            self.options[keystroke]()


def main():
    model = Model()
    viewer = Viewer(model)
    controller = Controller(model, viewer)

    # viewer.displayGrid()
    while True:
        keystrokes = raw_input('')
        for keystroke in keystrokes.split(' '):
            controller.exec_command(keystroke)

    # controller.execCommand('p')

if __name__=='__main__':
    main()