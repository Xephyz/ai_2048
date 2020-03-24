# The actual 2048 game!
# Why have we only done this now?
from logic import new_matrix, add_random_tile, left, right, down, up, print_board

class Game:
    """The actual 2048 game class"""
    def __init__(self, initial_board: list = new_matrix(4)):
        self.board = initial_board

    def move(self, move: str) -> None:
        if move == 'l': self.board = add_random_tile(left(self.board))
        if move == 'r': self.board = add_random_tile(right(self.board))
        if move == 'd': self.board = add_random_tile(down(self.board))
        if move == 'u': self.board = add_random_tile(up(self.board))
        print_board(self.board)