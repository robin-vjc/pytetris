__author__ = 'Robin'
"""
Graphical interface for pyTetris
"""

from Setup import *
import random

clock = pygame.time.Clock()
t_1 = 1
t_2 = 1

# Start the game with a random tetramino
controller.exec_command(random.choice(TETRAMINOS))

while True:
    clock.tick(RATE)

    # commands to be executed every 1 sec
    if not t_1 % RATE:
        # check if the active tetramino has settled, create a new one (random)
        if np.all(model.active_grid == '.'):
            controller.exec_command(random.choice(TETRAMINOS))
        controller.exec_command('s')  # check for lines to be cleared
        controller.exec_command('v')  # move down active tetramino one step
        draw_grid()
        t_1 = 0
    t_1 += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                controller.exec_command('<')
                draw_grid()
            elif event.key == K_RIGHT:
                controller.exec_command('>')
                draw_grid()
            elif event.key == K_DOWN:
                controller.exec_command('v')
                draw_grid()
            elif event.key == K_x:
                controller.exec_command('V')
                draw_grid()
            elif event.key == K_SPACE:
                controller.exec_command('!')
            elif event.key == K_a:
                controller.exec_command('(')
                draw_grid()
            elif event.key == K_d:
                controller.exec_command(')')
                draw_grid()
            elif event.key == K_p:
                draw_grid()
            elif event.key == K_ESCAPE:
                sys.exit()

    pygame.display.update()