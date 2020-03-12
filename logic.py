"""
This file contains all logic for handling a 2048 game.
We view the game board as an n*n matrix
"""

from copy import deepcopy
from random import randint, uniform

def new_matrix(size: int) -> list:
    return [[0 for _ in range(size)] for _ in range(size)]

def add_random_tile(board: list) -> list:
    new = deepcopy(board)
    x, y = [randint(0, len(board)-1) for _ in range(2)]
    while new[x][y] != 0:
        x, y = [randint(0, len(board)-1) for _ in range(2)]
    new[x][y] = 2 if uniform(0,1) > 0.1 else 4
    return new

def _transpose(mat: list) -> list:
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat))]

def _reverse(mat: list) -> list:
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
    new = deepcopy(mat)
    for x in range(len(mat)):
        for y in range(len(mat)-1):
            if new[x][y] == new[x][y+1] and new[x][y] != 0:
                new[x][y] *= 2
                new[x][y+1] = 0
    return new

def up(board: list) -> list:
    return _transpose(_compress(_merge(_compress(_transpose(board)))))

def down(board: list) -> list:
    return _transpose(_reverse(_compress(_merge(_compress(_reverse(_transpose(board)))))))

def left(board: list) -> list:
    return _compress(_merge(_compress(board)))

def right(board: list) -> list:
    return _reverse(_compress(_merge(_compress(_reverse(board)))))


if __name__ == "__main__":
    from pprint import pprint
    from sys import platform
    import os
    import time

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
        pprint(game)
        old = deepcopy(game)
        print("\nControls are wasd")
        turn = input("Move: ")
        if turn.lower() == "w": game=up(game)
        elif turn.lower() == "a": game=left(game)
        elif turn.lower() == "s": game=down(game)
        elif turn.lower() == "d": game=right(game)
        elif turn.lower() == "q": break
        if not game == old: game = add_random_tile(game)