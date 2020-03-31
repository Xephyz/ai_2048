from logic import transpose as tr, reverse as rev, check_game as cg

pattern = [[16,  9,   8,  1],
          [15,  10,  7,  2],
          [14,  11,  6,  3],
          [13,  12,  5,  4]]


def _build_patterns(p1: list = pattern):
    p2 = tr(p1)
    p3 = tr(rev(p2))
    p4 = rev(tr(p1))
    p5 = rev(tr(rev(tr(p4))))
    p6 = tr(p5)
    p7 = rev(p5)
    p8 = tr(p7)
    return [p1, p2, p3, p4, p5, p6, p7, p8]

patterns = _build_patterns()

def _get_state_value(state: list):
    sums = [0]*len(patterns)

    for i in range(len(state)):
        for j in range(len(state)):
            for k in range(len(patterns)):
                sums[k] += patterns[k][i][j] * state[i][j]

    return max(sums)

def evaluate(state: list):
    if cg(state) == -1: return -1000
    evalue = _get_state_value(state)
    if cg(state) == 1: return evalue + 1000
    else: return evalue

