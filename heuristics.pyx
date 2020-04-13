import cython
cimport cython

from logic import transpose as tr, reverse as rev, check_game as cg
from logic cimport transpose as tr, reverse as rev, check_game as cg

cdef list pattern = \
        [[16,   9,  8,  1],
         [15,  10,  7,  2],
         [14,  11,  6,  3],
         [13,  12,  5,  4]]


cdef list _build_patterns(list p1 = pattern):
    p2 = tr(p1)  # NW-E
    p3 = rev(p1)  # NE-S
    p4 = rev(p2)  # NE-W
    p5 = tr(p4)  # SW-N
    p6 = tr(p3)  # SW-E
    p7 = rev(p5)  # SE-N
    p8 = tr(p7)  # SE-W
    return [p1, p2, p3, p4, p5, p6, p7, p8]


cdef list patterns = _build_patterns()


cdef double _get_state_value(list state):
    cdef int i, j, k, state_len = len(state)
    cdef list sums = [0] * 8  # 8 represents 'len(patterns)', which is always 8

    for i in range(state_len):
        for j in range(state_len):
            for k in range(8):
                sums[k] += patterns[k][i][j] * state[i][j]

    return max(sums)


cpdef double evaluate(list state):
    if cg(state) == -1: return -1000
    cdef double evalue = _get_state_value(state)
    if cg(state) == 1: return evalue + 1000
    else: return evalue
