import cython
cimport cython

cpdef list new_matrix(int size=*)

@cython.locals(x=cython.int, y=cython.int)
cpdef list add_random_tile(list board)

@cython.locals(i=cython.int)
cpdef int check_game(list board)

@cython.locals(i=cython.int, j=cython.int)
cpdef list transpose(list mat)

@cython.locals(i=cython.int, j=cython.int)
cpdef list reverse(list mat)

cdef list _compress(list mat)

@cython.locals(x=cython.int, y=cython.int, new=list)
cdef list _merge(list mat)

cpdef list up(list board)
cpdef list down(list board)
cpdef list left(list board)
cpdef list right(list board)

@cython.locals(row=cython.int, tile=cython.int)
cpdef get_possible_states(list board)
