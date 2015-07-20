from Tetramino import *
import copy

Position = namedtuple('Position', ['row','col'])

class Model(object):
    "model stores grid state, pieces and their position"
    GRID_ROWS = 22
    GRID_COLS = 10
    # level up settings
    LEVEL_UP = 1000  # level goes up every 1000 score
    MAX_LEVEL = 29

    def __init__(self):
        self.grid = np.empty((self.GRID_ROWS, self.GRID_COLS), dtype=str)
        self.grid[:,:] = '.'
        self.active_grid = np.empty((self.GRID_ROWS, self.GRID_COLS), dtype=str)
        self.active_grid[:,:] = '.'
        self.tetraminos = []
        self.active_tetramino = Tetramino()
        self.score = 0
        self.cleared_lines = 0
        self.level = 0
        self._observers = []
        self.game_mode = 'board'  # can be board, menu, pause

    def add_tetramino(self, tetramino):
        """ appends input Tetramino to model, and adds it to the model.active_grid
        :param tetramino: Tetramino to be added
        :return: None
        """
        self.tetraminos.append(tetramino)
        self.active_tetramino = tetramino
        # insert tetramino in the active grid at the initiation position
        self.move_active_tetramino(tetramino.position)


    def check_wall_collision(self, position, tetramino):
        """ check for wall collision
        :param position: tenative position of the tetramino
        :param tetramino: tetramino to be checked
        :return: True if position is within walls, False otherwise
        """
        blocks_row, blocks_col = np.where(tetramino.piece_grid != '.')
        if (position.col+blocks_col.min() >= 0) \
                and (position.col+blocks_col.max() <= self.GRID_COLS-1) \
                and (position.row+blocks_row.max() <= self.GRID_ROWS-1):
            return True
        else:
            return False

    def check_unit_collision(self, position, tetramino):
        """ check for unit collision
        :param position: tenative position of the tetramino
        :param tetramino: tetramino to be checked
        :return: True if position does NOT collide with settled units, False otherwise
        """
        # local position of the filled blocks
        blocks_row, blocks_col = np.where(tetramino.piece_grid != '.')
        # global position of the blocks in the grid
        blocks_row = [x+position.row for x in blocks_row]
        blocks_col = [x+position.col for x in blocks_col]

        return all(self.grid[blocks_row,blocks_col]=='.')

    def move_active_tetramino(self, position):
        """ move the active tetramino at the given position
        :param position: tentative new position for the tetramino
        :return: True if movement was successful, False otherwise
        """
        # if wall/unit collision is OK, return false if it fails
        if self.check_wall_collision(position, self.active_tetramino) and \
                self.check_unit_collision(position, self.active_tetramino):
            self.active_tetramino.position = position
            self.update_active_grid()
            return True
        # couldn't move? was it trying to move downwards?
        elif position.row > self.active_tetramino.position.row:
            # stuck in the first two rows? -> game over!
            if self.active_tetramino.position.row < 2:
                self.settle_active_tetramino()
                self.game_mode = 'game over'
            # otherwise settle it
            # TODO leave uncommented..?
            else:
                self.settle_active_tetramino()
            return False
        else:
            return False

    def update_active_grid(self):
        piece_grid = self.active_tetramino.piece_grid
        position = self.active_tetramino.position
        # clear active grid first, then replace
        self.active_grid[:,:] = '.'
        for i, entry in enumerate(np.where(piece_grid != '.')[0]):
            r = np.where(piece_grid != '.')[0][i] # row of non-empty entry
            c = np.where(piece_grid != '.')[1][i] # col of non-empty entry
            self.active_grid[position.row+r, position.col+c] = np.char.capitalize(piece_grid[r,c])

    def step(self):
        # if row is complete, erase it
        for i, row in enumerate(self.grid):
            if '.' not in row:
                # erase row
                self.grid[i][:] = ['.']*self.GRID_COLS
                # move existing grid above cancelled row one step down
                temp_grid = np.empty((self.GRID_ROWS,self.GRID_COLS), dtype=str)
                temp_grid[:,:] = '.'
                for i_temp, row_temp in enumerate(temp_grid):
                    if i_temp <= i and i_temp >= 1:
                        temp_grid[i_temp][:] = self.grid[i_temp-1][:]
                    else:
                        temp_grid[i_temp][:] = self.grid[i_temp][:]
                self.grid = temp_grid
                self.cleared_lines += 1
                self.score += 100

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
        """ move active tetramino one step downward """
        old_row = self.active_tetramino.position.row
        new_position = self.active_tetramino.position._replace(row=old_row+1)
        self.move_active_tetramino(new_position)

    def move_downward_deep(self):
        """ move tetramino at the bottom """
        position = self.active_tetramino.position
        while self.move_active_tetramino(position):
            self.move_active_tetramino(position)
            position = position._replace(row=position.row+1)
        self.settle_active_tetramino()

    def rotate_right(self):
        # if it is OK rotate, rotate
        test_tetramino = copy.deepcopy(self.active_tetramino)
        test_tetramino.rotate_right()
        if self.check_wall_collision(test_tetramino.position, test_tetramino) and \
                self.check_unit_collision(test_tetramino.position, test_tetramino):
            self.active_tetramino.rotate_right()
            self.update_active_grid()

    def rotate_left(self):
        # if it is OK rotate, rotate
        test_tetramino = copy.deepcopy(self.active_tetramino)
        test_tetramino.rotate_left()
        if self.check_wall_collision(test_tetramino.position, test_tetramino) and \
                self.check_unit_collision(test_tetramino.position, test_tetramino):
            self.active_tetramino.rotate_left()
            self.update_active_grid()
        # otherwise pass

    def test_tetramino(self):
        self.active_tetramino.test_tetramino()

    def settle_active_tetramino(self):
        """ pushes active tetramino into the settle grid model.grid """
        piece_grid = self.active_tetramino.piece_grid
        position = self.active_tetramino.position
        # push tetramino into settled grid
        for i, entry in enumerate(np.where(piece_grid != '.')[0]):
            r = np.where(piece_grid != '.')[0][i] # row of non-empty entry
            c = np.where(piece_grid != '.')[1][i] # col of non-empty entry
            self.grid[position.row+r, position.col+c] = piece_grid[r,c]
        # clear active grid
        self.active_grid[:,:] = '.'

    def set_mode(self, setting='!'):
        """ sets the current view to either menu or game board
        :param setting: '!' sets game mode, '@' sets menu
        :return: None
        """
        # if game mode is in board, '!' pauses
        if (setting == '!') and (self.game_mode == 'board'):
            self.game_mode = 'pause'
        elif setting == '!':
            self.game_mode = 'board'
        elif setting == '@':
            self.game_mode = 'menu'

    def update_level(self):
        # increase level every +model.LEVEL_UP score; max level is model.MAX_LEVEL
        self.level = min(int(self.score/self.LEVEL_UP), self.MAX_LEVEL)

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

    def display_status(self):
        if self.model.game_mode == 'board':
            self.display_active_grid()
        elif self.model.game_mode == 'menu':
            print 'Learntris (c) 1992 Tetraminex, Inc.'
            print 'Press start button to begin.'
        elif self.model.game_mode == 'pause':
            print 'Paused'
            print 'Press start button to continue.'
        elif self.model.game_mode == 'game over':
            self.display_active_grid()
            print 'Game Over'
        else:
            pass

    def display_active_grid(self):
        """ displays active piece, AND settled pieces """
        # merge settled grid
        merged_grid = copy.deepcopy(self.model.grid)
        # with the active piece grid
        act_blocks_row, act_blocks_col = np.where(self.model.active_grid!='.')
        merged_grid[act_blocks_row,act_blocks_col] = \
            self.model.active_grid[act_blocks_row,act_blocks_col]
        for row in range(self.model.GRID_ROWS):
            print ' '.join(merged_grid[row])

        if self.model.game_mode == 'game over':
            print 'Game Over'

    def display_score(self):
        print self.model.score

    def display_cleared_lines(self):
        print self.model.cleared_lines

    def update(self, model):
        "what to do when model is updated"
        self.display_active_grid()


class Controller(object):

    def given_grid(self):
        temp_grid = self.model.grid
        for i in range(self.model.GRID_ROWS):
            input_row = raw_input('')
            temp_grid[i][:] = input_row.split(' ')
        self.model.grid = temp_grid

    def clear_grid(self):
        self.model.grid = np.empty((self.model.GRID_ROWS, self.model.GRID_COLS), dtype=str)
        self.model.grid[:,:] = '.'



    def print_empty_line(self):
        print ''

    def __init__(self, model, viewer):
        self.model = model
        self.viewer = viewer

        self.options = {'q': quit,
                        '@': self.model.set_mode,
                        '!': self.model.set_mode,
                        'p': self.viewer.display_status,
                        'P': self.viewer.display_active_grid,
                        'g': self.given_grid,
                        'c': self.clear_grid,
                        's': self.model.step,
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
                        '(': self.model.rotate_left,
                        '<': self.model.move_left,
                        '>': self.model.move_right,
                        'v': self.model.move_downward,
                        'V': self.model.move_downward_deep,
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
        elif keystroke == '@':
            self.options[keystroke]('@')
        elif keystroke == '!':
            self.options[keystroke]('!')
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