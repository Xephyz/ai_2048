# The actual 2048 game!
# Why have we only done this now?
from logic import new_matrix, add_random_tile, left, right, down, up, print_board

class Game:
    """The actual 2048 game class"""
    def __init__(self, initial_board: list = new_matrix(4)):
        self.board = add_random_tile(add_random_tile(initial_board))

    def move(self, move: str) -> None:
        if move == 'l':
            print('Going left')
            self.board = add_random_tile(left(self.board)) if left(self.board) != self.board else self.board
        elif move == 'r':
            print('Going right')
            self.board = add_random_tile(right(self.board)) if right(self.board) != self.board else self.board
        elif move == 'd':
            print('Going down')
            self.board = add_random_tile(down(self.board)) if down(self.board) != self.board else self.board
        elif move == 'u':
            print('Going up')
            self.board = add_random_tile(up(self.board)) if up(self.board) != self.board else self.board
