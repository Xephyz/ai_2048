from logic import transpose as tr, reverse as rev, check_game as cg

# testsnek = [[20,  9, 4, .1],
#             [19, 10, 3, .2],
#             [18, 11, 2, .3],
#             [17, 12, 1, .4]]

snake1 = [[16,  9,   8,  1],
          [15,  10,  7,  2],
          [14,  11,  6,  3],
          [13,  12,  5,  4]]


def _build_sneks(p1: list = snake1):
    p2 = tr(p1)
    p3 = tr(rev(p2))
    p4 = rev(tr(p1))
    p5 = rev(tr(rev(tr(p4))))
    p6 = tr(p5)
    p7 = rev(p5)
    p8 = tr(p7)
    return [p1, p2, p3, p4, p5, p6, p7, p8]


class AI():
    def __init__(self, init_matrix: list = snake1):
        self._weight_matrix = _build_sneks(init_matrix)

    def evaluate(self, state: list):
        if cg(state) == -1: return -1000
        evalue = self._get_state_value(state)
        if cg(state) == 1: return evalue + 1000
        else return evalue

    def _get_state_value(self, state: list):
        sums = [0]*len(self._weight_matrix)

        for i in range(len(state)):
            for j in range(len(state)):
                for k in range(len(self._weight_matrix)):
                    sums[k] += self._weight_matrix[k][i][j] * state[i][j]

        return max(sums)

