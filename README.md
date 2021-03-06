# pytetris
Python implementation of the Tetriss game, following the challenge @ [GitHub](https://github.com/LearnProgramming/learntris).

### Running the game
To start the game, simply run **gui.py**.
* `movement arrows` move the pieces left, right and downwards
* `a` and `d` rotate the piece
* `x` moves the piece to the bottom

<img align="middle" src="./images/screenshot_3.png" alt="Screenshot">

### Console

It is also possible to run **tetris.py** from console, and control it using the following commands:
* `q`: quits the game
* `@`: sets the game at the menu
* `!`: starts/pauses the game
* `p`: prints the current status (menu, pause, or current grid depending on the status)
* `P`: displays the grid with only the active piece
* `g`: takes as input a given grid
* `c`: clears the grid
* `s`: steps (checks for full lines)
* `?s`: displays score
* `?n`: displays number of cleared lines
* `I`: adds an 'I' tetramino
* `J`: adds a 'J' tetramino
* `L`: adds an 'L' tetramino
* `O`: adds an 'O' tetramino
* `S`: adds an 'S' tetramino
* `T`: adds a 'T' tetramino
* `Z`: adds a 'Z' tetramino
* `)`: rotates active tetramino clockwise
* `(`: rotates active tetramino counter clockwise
* `<`: moves active tetramino to the left
* `>`: moves active tetramino to the right
* `v`: moves active tetramino one step down
* `V`: moves active tetramino to the bottom
* `t`: displayes local grid of the active tetramino
* `;`: prints an empty line

The file **tetris.py** will also pass all the tests of the challenge.
