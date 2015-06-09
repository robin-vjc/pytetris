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
        # insert tetramino in the active grid at the initiation position
        self.move_active_tetramino(tetramino.position)

    def check_wall_collision(self, position, tetramino):
        """ returns True if given position is within walls (OK), False otherwise """
        blocks_row, blocks_col = np.where(tetramino.piece_grid != '.')
        if (position.col+blocks_col.min() >= 0) \
                and (position.col+blocks_col.max() <= self.gridColumns) \
                and (position.row+blocks_row.max() <= self.gridRows):
            return True
        else:
            return False

    def move_active_tetramino(self, position):
        """ move the active tetramino at the given position """
        # check if wall collision is OK, don't do anything if it fails
        if self.check_wall_collision(position, self.active_tetramino):
            self.active_tetramino.position = position
            self.update_active_grid()
        else:
            pass

    def update_active_grid(self):
        t_rows = self.active_tetramino.piece_grid.shape[0]
        t_cols = self.active_tetramino.piece_grid.shape[1]
        position = self.active_tetramino.position
        # clear active grid first, then replace
        self.active_grid[:,:] = '.'
        self.active_grid[position.row:position.row+t_rows, position.col:position.col+t_cols]\
                = np.char.capitalize(self.active_tetramino.piece_grid)

    def move_left(self):
        """ move active tetramino one step to the left """
        old_column = self.active_tetramino.position.col
        new_position = self.active_tetramino.position._replace(col=old_column-1)
        self.move_active_tetramino(new_position)

    def move_right(self):
        """ move active tetramino one step to the right """
        old_column = self.active_tetramino.position.col
        new_position = self.active_tetramino.position._replace(col=old_column+1)
        self.move_active_tetramino(new_position)

    def move_downward(self):
        """ move active tetramino one step to the right """
        old_row = self.active_tetramino.position.row
        new_position = self.active_tetramino.position._replace(row=old_row+1)
        self.move_active_tetramino(new_position)

    def rotate_right(self):
        # here it should be checked whether the rotation is OK
        # if it is OK rotate
        # otherwise pass
        self.active_tetramino.rotate_right()
        self.update_active_grid()

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
                        '<': self.model.move_left,
                        '>': self.model.move_right,
                        'v': self.model.move_downward,
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

    while True:
        keystrokes = raw_input('')
        # commands are separated by either: newline, blank space,
        # or nothing (and have to be parsed); the following logic
        # finds commands that start with '?' and parses them; regexp
        # here may be better
        for keystroke_cluster in keystrokes.split(' '):
            i = 0
            while i < keystroke_cluster.__len__():
                if keystroke_cluster[i] == '?':
                    controller.exec_command(keystroke_cluster[i:i+2])
                    i += 1
                else:
                    controller.exec_command(keystroke_cluster[i])
                i += 1

if __name__=='__main__':
    main()