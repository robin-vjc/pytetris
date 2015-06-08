from Tetramino import *

Position = namedtuple('Position', ['row','col'])

class Model(object):
    "model stores grid state, pieces and their position"
    gridRows = 22
    gridColumns = 10

    def __init__(self):
        self.grid = np.empty((self.gridRows, self.gridColumns), dtype=str)
        self.grid[:,:] = '.'
        self.active_grid = np.empty((self.gridRows, self.gridColumns), dtype=str)
        self.active_grid[:,:] = '.'
        self.tetraminos = []
        self.active_tetramino = Tetramino()
        self.score = 0
        self.cleared_lines = 0
        self._observers = []

    def add_tetramino(self, tetramino):
        self.tetraminos.append(tetramino)
        self.active_tetramino = tetramino
        self.move_active_tetramino(tetramino.position)

    def move_active_tetramino(self, position):
        """ move the active tetramino at the given position """
        t_rows = self.active_tetramino.piece_grid.shape[0]
        t_cols = self.active_tetramino.piece_grid.shape[1]
        # clear active grid first, then move
        self.active_grid[:,:] = '.'
        # TODO here there should be more logic to see if you can actually move it or not
        self.active_grid[position.row:position.row+t_rows, position.col:position.col+t_cols] = np.char.capitalize(self.active_tetramino.piece_grid)

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

    def display_active_grid(self):
        for row in range(self.model.gridRows):
            print ' '.join(self.model.active_grid[row])

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
        self.model.grid = np.empty((self.model.gridRows, self.model.gridColumns), dtype=str)
        self.model.grid[:,:] = '.'

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
                        'P': self.viewer.display_active_grid,
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
        #for keystroke_cluster in keystrokes.split(' '):
        #    for keystroke in list(keystroke_cluster):
        for keystroke in keystrokes.split(' '):
            controller.exec_command(keystroke)

    # controller.execCommand('p')

if __name__=='__main__':
    main()