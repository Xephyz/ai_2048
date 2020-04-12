# 2048 game!
import cython
from logic import new_matrix, add_random_tile, left, right, down, up

cimport cython
from logic cimport new_matrix, add_random_tile, left, right, down, up


cdef class Game:
    """The actual 2048 game class"""
    cdef public list board

    def __cinit__(self, list initial_board = new_matrix(4)):
        self.board = add_random_tile(add_random_tile(initial_board))

    def __init__(self, list initial_board = new_matrix(4)):
        self.board = add_random_tile(add_random_tile(initial_board))

    cpdef move(self, str move):
        if move == 'l':
            print('Going left\n')
            self.board = add_random_tile(left(self.board)) if left(self.board) != self.board else self.board
        elif move == 'r':
            print('Going right\n')
            self.board = add_random_tile(right(self.board)) if right(self.board) != self.board else self.board
        elif move == 'd':
            print('Going down\n')
            self.board = add_random_tile(down(self.board)) if down(self.board) != self.board else self.board
        elif move == 'u':
            print('Going up\n')
            self.board = add_random_tile(up(self.board)) if up(self.board) != self.board else self.board
