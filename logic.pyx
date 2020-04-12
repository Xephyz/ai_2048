"""
This file contains all logic for handling a 2048 game.
We view the game board as an n*n matrix
"""

from random import randint, uniform


cpdef list new_matrix(int size = 4):
    return [[0] * size] * size


cpdef list add_random_tile(list board):
    cdef int x, y
    new = [list(row) for row in board]
    x, y = [randint(0, len(board) - 1) for _ in range(2)]
    while new[x][y] != 0:
        x, y = [randint(0, len(board) - 1) for _ in range(2)]
    new[x][y] = 2 if uniform(0, 1) > 0.1 else 4
    return new


cpdef int check_game(list board):
    cdef int i
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


cpdef list transpose(list mat):
    cdef int i, j
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat))]


cpdef list reverse(list mat):
    cdef int i, j
    return [[mat[j][i] for i in range(len(mat) - 1, -1, -1)] for j in range(len(mat))]


cdef list _compress(list mat):
    return [sorted(row, key=lambda x: not x) for row in mat]


cdef list _merge(list mat):
    cdef int x, y
    cdef list new = [list(row) for row in mat]
    for x in range(len(mat)):
        for y in range(len(mat) - 1):
            if new[x][y] == new[x][y + 1] and new[x][y] != 0:
                new[x][y] *= 2
                new[x][y + 1] = 0
    return new


cpdef list up(list board):
    return transpose(_compress(_merge(_compress(transpose(board)))))


cpdef list down(list board):
    return transpose(reverse(_compress(_merge(_compress(reverse(transpose(board)))))))


cpdef list left(list board):
    return _compress(_merge(_compress(board)))


cpdef list right(list board):
    return reverse(_compress(_merge(_compress(reverse(board)))))


def print_board(list board, str endl = '\n\n\n') -> None:
    cdef int i, j
    result = ""
    for i in range(len(board)):
        for j in range(len(board)):
            result += f'{board[i][j]}\t' if board[i][j] != 0 else '.\t'
        result += endl if i < len(board) - 1 else ''
    print(result)


cpdef get_possible_states(list board):
    cdef int row, tile
    twos = []
    fours = []
    for row in range(len(board)):
        for tile in range(len(board)):
            if not board[row][tile]:
                twos.append([list(row) for row in board])
                fours.append([list(row) for row in board])
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
        old = [list(row) for row in game]
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
