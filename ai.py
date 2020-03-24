# Ai does gaem veri gut yes

from game import Game
from logic import left, right, down, up, print_board as pb
from expectimax import expectimax as exp
from sys import platform
from os import system
from time import sleep

if __name__ == "__main__":
    clear_cmd = 'cls' if platform == 'win32' else 'clear'

    g = Game()
    d = 3  # default depth
    # g.board = [[2,16,0,2],[2,8,4,8],[4,256,64,32],[1024,4,128,4]]
    print('Starting, now!')

    while True:
        # system(clear_cmd)
        # pb(g.board)

        pos_moves = []
        pos_moves.append(exp(left(g.board), d) if left(g.board) != g.board else -1001)
        pos_moves.append(exp(right(g.board), d) if right(g.board) != g.board else -1001)
        pos_moves.append(exp(down(g.board), d) if down(g.board) != g.board else -1001)
        pos_moves.append(exp(up(g.board), d) if up(g.board) != g.board else -1001)

        best_move = pos_moves.index(max(pos_moves))
        if max(pos_moves) == -1001:
            print('Game over')
            pb(g.board)
            break

        system(clear_cmd)
        if best_move == 0: g.move('l')
        elif best_move == 1: g.move('r')
        elif best_move == 2: g.move('d')
        else: g.move('u')
        print(pos_moves)
        pb(g.board)

        sleep(0.5)