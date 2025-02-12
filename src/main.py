import pyxel
from board import Board

my_board = Board(200, 250)
pyxel.run(my_board.update, my_board.draw)
