# Expectimax algorithm!
from logic import check_game, get_possible_states, up, down, left, right
from heuristics import evaluate

def expectimax(board: list, depth: int = 2):
    if depth == 0 or check_game(board) == -1:
        return evaluate(board)
    elif d % 2 != 0:
        return max(expectimax(left(board), depth-1), 
                   expectimax(right(board), depth-1), 
                   expectimax(down(), depth-1),
                   expectimax(up(board), depth-1))
    else:
        sum2, sum4 = (0, 0)
        twos, fours = get_possible_states(board)
        for state2 in twos: sum2 += expectimax(state2)
        for state4 in fours: sum4 += expectimax(state4)
        return (0.9 * sum2 + 0.1 * sum4)/len(twos)