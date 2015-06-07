from collections import namedtuple

Position = namedtuple('Position', ['row','column'])
Block = namedtuple('Block', ['row', 'column', 'color'])

class Tetramino(object):
    "Tetramino object subclasses all the tetraminos"
    piece_grid_rows = 1
    piece_grid_cols = 1
    piece_orientations = 1

    def __init__(self, position=Position(0,0)):
        self.position = position
        self.orientation = 0
        # orientations_grid[orientation][row][column]
        self.orientations_grid = [[['.' for i in range(self.piece_grid_cols)]\
                                  for j in range(self.piece_grid_rows)]\
                                  for k in range(self.piece_orientations)]
        self.piece_grid = self.rotate(self.orientation)

    def display_piece_grid(self):
        for row in range(self.piece_grid_rows):
            print ' '.join(self.piece_grid[row])

    def test_tetramino(self):
        self.display_piece_grid()

    def rotate(self, orientation):
        self.piece_grid = self.orientations_grid[orientation][:][:]
        return self.piece_grid

class I_Tetramino(Tetramino):
    """ Implementation of the I Tetramino
    orientation: 0 = horizontal, 1 = vertical """
    piece_grid_rows = 4
    piece_grid_cols = 4
    piece_orientations = 2

    def __init__(self, position=Position(0,0)):
        Tetramino.__init__(self, position)
        # orientation 0
        self.orientations_grid[0][1][:] = ['c','c','c','c']
        self.piece_grid = self.rotate(self.orientation)

class O_Tetramino(Tetramino):
    """ Implementation of the O Tetramino """
    piece_grid_rows = 2
    piece_grid_cols = 2
    piece_orientations = 1

    def __init__(self, position=Position(0,0)):
        Tetramino.__init__(self, position)
        # orientation 0: 2x2 square 'y' (first row, then second row)
        self.orientations_grid[0][0][:] = ['y','y']
        self.orientations_grid[0][1][:] = ['y','y']
        self.piece_grid = self.rotate(self.orientation)

class Z_Tetramino(Tetramino):
    """ Implementation of the Z Tetramino """
    piece_grid_rows = 3
    piece_grid_cols = 3
    piece_orientations = 2

    def __init__(self, position=Position(0,0)):
        Tetramino.__init__(self, position)
        # orientation 0
        self.orientations_grid[0][0][:] = ['r','r','.']
        self.orientations_grid[0][1][:] = ['.','r','r']
        self.piece_grid = self.rotate(self.orientation)

class S_Tetramino(Tetramino):
    """ Implementation of the S Tetramino """
    piece_grid_rows = 3
    piece_grid_cols = 3
    piece_orientations = 2

    def __init__(self, position=Position(0,0)):
        Tetramino.__init__(self, position)
        # orientation 0
        self.orientations_grid[0][0][:] = ['.','g','g']
        self.orientations_grid[0][1][:] = ['g','g','.']
        self.piece_grid = self.rotate(self.orientation)

class J_Tetramino(Tetramino):
    """ Implementation of the J Tetramino """
    piece_grid_rows = 3
    piece_grid_cols = 3
    piece_orientations = 2

    def __init__(self, position=Position(0,0)):
        Tetramino.__init__(self, position)
        # orientation 0
        self.orientations_grid[0][0][:] = ['b','.','.']
        self.orientations_grid[0][1][:] = ['b','b','b']
        self.piece_grid = self.rotate(self.orientation)

class L_Tetramino(Tetramino):
    """ Implementation of the J Tetramino """
    piece_grid_rows = 3
    piece_grid_cols = 3
    piece_orientations = 2

    def __init__(self, position=Position(0,0)):
        Tetramino.__init__(self, position)
        # orientation 0
        self.orientations_grid[0][0][:] = ['.','.','o']
        self.orientations_grid[0][1][:] = ['o','o','o']
        self.piece_grid = self.rotate(self.orientation)

class T_Tetramino(Tetramino):
    """ Implementation of the J Tetramino """
    piece_grid_rows = 3
    piece_grid_cols = 3
    piece_orientations = 2

    def __init__(self, position=Position(0,0)):
        Tetramino.__init__(self, position)
        # orientation 0
        self.orientations_grid[0][0][:] = ['.','.','o']
        self.orientations_grid[0][1][:] = ['o','o','o']
        self.piece_grid = self.rotate(self.orientation)


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
                        'Z': self.model.add_tetramino,
                        't': self.model.test_tetramino}

    def exec_command(self, keystroke):
        if keystroke == 'I':
            self.options[keystroke](I_Tetramino())
        elif keystroke == 'J':
            self.options[keystroke](J_Tetramino())
        elif keystroke == 'L':
            self.options[keystroke](L_Tetramino())
        elif keystroke == 'O':
            self.options[keystroke](O_Tetramino())
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