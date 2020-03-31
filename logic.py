"""
This file contains all logic for handling a 2048 game.
We view the game board as an n*n matrix
"""

from random import randint, uniform


def new_matrix(size: int = 4) -> list:
    return [[0] * size] * size


def add_random_tile(board: list) -> list:
    new = [[item for item in row] for row in board]
    x, y = [randint(0, len(board) - 1) for _ in range(2)]
    while new[x][y] != 0:
        x, y = [randint(0, len(board) - 1) for _ in range(2)]
    new[x][y] = 2 if uniform(0, 1) > 0.1 else 4
    return new


def check_game(board: list) -> int:
    """Checks game state: 
    returns: 
         1 if game is won
        -1 if game is lost
         0 if neither
    """
    # Check game is "won"
    for row in board:
        if 2048 in row: return 1

    # Quicker check game is not lost
    for row in board:
        if 0 in row: return 0

    # Slow check
    for row in board:
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]: return 0
    for row in transpose(board):
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]: return 0
    return -1


def transpose(mat: list) -> list:
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat))]


def reverse(mat: list) -> list:
    return [[mat[j][i] for i in range(len(mat) - 1, -1, -1)] for j in range(len(mat))]


def _compress(mat: list) -> list:
    return [sorted(row, key=lambda x: not x) for row in mat]


def _merge(mat: list) -> list:
    new = [[item for item in row] for row in mat]
    for x in range(len(mat)):
        for y in range(len(mat) - 1):
            if new[x][y] == new[x][y + 1] and new[x][y] != 0:
                new[x][y] *= 2
                new[x][y + 1] = 0
    return new


def up(board: list) -> list:
    return transpose(_compress(_merge(_compress(transpose(board)))))


def down(board: list) -> list:
    return transpose(reverse(_compress(_merge(_compress(reverse(transpose(board)))))))


def left(board: list) -> list:
    return _compress(_merge(_compress(board)))


def right(board: list) -> list:
    return reverse(_compress(_merge(_compress(reverse(board)))))


def print_board(board: list, endl: str = '\n') -> None:
    result = ""
    for i in range(len(board)):
        for j in range(len(board)):
            result += f'{board[i][j]}\t' if board[i][j] != 0 else '.\t'
        result += endl if i < len(board) - 1 else ''
        result += "\n\n"
    print(result)


def get_possible_states(board: list) -> tuple:
    twos = []
    fours = []
    for row in range(len(board)):
        for tile in range(len(board)):
            if not board[row][tile]:
                twos.append(board)
                fours.append(board)
                twos[-1][row][tile] = 2
                fours[-1][row][tile] = 4
    return twos, fours


'''
# Game for human
if __name__ == "__main__":
    from pprint import pprint
    from sys import platform
    import os

    points = 0

    clear_cmd = 'clear' if platform != "win32" else 'cls'
    print("How large do you want the board to be?")
    size = int(input("Size: "))
    print("Creating game...")
    game = new_matrix(size)
    game = add_random_tile(add_random_tile(game))

    while True:
        os.system(clear_cmd)
        print(f'points: {points}')
        # pprint(game, width=20)
        print_board(game)
        old = [[item for item in row] for row in game]
        print("\nControls are wasd")
        turn = input("Move: ")
        if turn.lower() == "w":
            game = up(game)
        elif turn.lower() == "a":
            game = left(game)
        elif turn.lower() == "s":
            game = down(game)
        elif turn.lower() == "d":
            game = right(game)
        elif turn.lower() == "q":
            break
        if not game == old: game = add_random_tile(game)
'''
