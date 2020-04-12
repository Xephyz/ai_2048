import cython
cimport cython

from logic import transpose as tr, reverse as rev, check_game as cg
from logic cimport transpose as tr, reverse as rev, check_game as cg

cdef list pattern = \
        [[16,  9,   8,  1],
        [15,  10,  7,  2],
        [14,  11,  6,  3],
        [13,  12,  5,  4]]


cdef list _build_patterns(list p1 = pattern):
    p2 = tr(p1)
    p3 = tr(rev(p2))
    p4 = rev(tr(p1))
    p5 = rev(tr(rev(tr(p4))))
    p6 = tr(p5)
    p7 = rev(p5)
    p8 = tr(p7)
    return [p1, p2, p3, p4, p5, p6, p7, p8]

cdef list patterns = _build_patterns()

cdef double _get_state_value(list state):
    cdef int i, j, k, state_len = len(state), patterns_len = len(patterns)
    cdef list sums = [0]*len(patterns)

    for i in range(state_len):
        for j in range(state_len):
            for k in range(patterns_len):
                sums[k] += patterns[k][i][j] * state[i][j]

    return max(sums)

cpdef double evaluate(list state):
    if cg(state) == -1: return -1000
    cdef double evalue = _get_state_value(state)
    if cg(state) == 1: return evalue + 1000
    else: return evalue

