"""
This file contains all logic for handling a 2048 game.
We view the game board as an n*n matrix
"""

from copy import deepcopy
from random import randint, uniform

# Global points
points: int = None

def new_matrix(size: int=4) -> list:
    return [[0 for _ in range(size)] for _ in range(size)]

def add_random_tile(board: list) -> list:
    new = deepcopy(board)
    x, y = [randint(0, len(board)-1) for _ in range(2)]
    while new[x][y] != 0:
        x, y = [randint(0, len(board)-1) for _ in range(2)]
    new[x][y] = 2 if uniform(0,1) > 0.1 else 4
    return new

def check_game(board: list) -> int:
    """Checks game state: 
    returns: 
        1  if game is won
        -1 if game is lost
        0  if neither
    """
    # result = 0
    # Check game is "won"
    for row in board:
        if 2048 in row: return 1

    # Quicker check game is not lost
    for row in board:
        if 0 in row: return 0
    
    # Slow check
    for row in board:
        for i in range(len(row)-1):
            if row[i] == row[i+1]: return 0
    for row in transpose(board):
        for i in range(len(row)-1):
            if row[i] == row[i+1]: return 0
    return -1


def transpose(mat: list) -> list:
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat))]

def reverse(mat: list) -> list:
    return [[mat[j][i] for i in range(len(mat)-1, -1, -1)] for j in range(len(mat))]

def _compress(mat: list) -> list:
    new = [[0 for _ in range(len(mat))] for _ in range(len(mat))]
    for x in range(len(mat)):
        count = 0
        for y in range(len(mat)):
            if mat[x][y] != 0:
                new[x][count] = mat[x][y]
                count += 1
    return new

def _merge(mat: list) -> list:
    global points
    new = deepcopy(mat)
    for x in range(len(mat)):
        for y in range(len(mat)-1):
            if new[x][y] == new[x][y+1] and new[x][y] != 0:
                new[x][y] *= 2
                if points is not None: points += new[x][y]
                new[x][y+1] = 0
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
        result += endl if i < len(board)-1 else ''
    print(result)

def get_possible_states(board: list) -> tuple:
    twos = []
    fours = []
    for row in range(len(board)):
        for tile in range(len(board)):
            if not board[row][tile]:
                twos.append(deepcopy(board))
                fours.append(deepcopy(board))
                twos[-1][row][tile] = 2
                fours[-1][row][tile] = 4
    return twos, fours


if __name__ == "__main__":
    from pprint import pprint
    from sys import platform
    import os
    import time

    points = 0

    # unix = input("Are you using Linux? (Y/n): ")
    clear_cmd = 'clear' if platform != "win32" else 'cls'
    print("How large do you want the board to be?")
    size = int(input("Size: "))
    print("Creating game...")
    game = new_matrix(size)
    game = add_random_tile(add_random_tile(game))
    time.sleep(0.5)

    while True:
        os.system(clear_cmd)
        print(f'points: {points}')
        # pprint(game, width=20)
        print_board(game)
        old = deepcopy(game)
        print("\nControls are wasd")
        turn = input("Move: ")
        if turn.lower() == "w": game=up(game)
        elif turn.lower() == "a": game=left(game)
        elif turn.lower() == "s": game=down(game)
        elif turn.lower() == "d": game=right(game)
        elif turn.lower() == "q": break
        if not game == old: game = add_random_tile(game)