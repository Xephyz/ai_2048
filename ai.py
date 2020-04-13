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
    dynamic_depth = True
    print('Starting, now!')

    while True:
        if dynamic_depth:
            zeroes = sum([row.count(0) for row in g.board])
            d = 7 if zeroes < 2 else 5 if zeroes < 4 else 3

        prev_board = [list(row) for row in g.board]

        pos_moves = []
        pos_moves.append(exp(left(g.board), d) if left(g.board) != g.board else -1001)
        pos_moves.append(exp(right(g.board), d) if right(g.board) != g.board else -1001)
        pos_moves.append(exp(down(g.board), d) if down(g.board) != g.board else -1001)
        pos_moves.append(exp(up(g.board), d) if up(g.board) != g.board else -1001)

        best_move = pos_moves.index(max(pos_moves))
        readable_moves = ['Invalid Move' if move == -1001 else
                          'Game Over' if move == -1000 else
                          f'{move:.0f}' for move in pos_moves]

        if max(pos_moves) == -1001:
            # system(clear_cmd)
            print('Game over\n')
            print(f'Left:\t{readable_moves[0]}\
                    \nRight:\t{readable_moves[1]}\
                    \nDown:\t{readable_moves[2]}\
                    \nUp:\t{readable_moves[3]}\n')
            pb(g.board)
            break

        system(clear_cmd)
        if best_move == 0:
            g.move('l')
        elif best_move == 1:
            g.move('r')
        elif best_move == 2:
            g.move('d')
        else:
            g.move('u')

        print(f'Left:\t{readable_moves[0]}\
                \nRight:\t{readable_moves[1]}\
                \nDown:\t{readable_moves[2]}\
                \nUp:\t{readable_moves[3]}\n')
        pb(prev_board)
