import cython
cimport cython

cdef list pattern

cdef list _build_patterns(list p1 = *)

cdef list patterns

@cython.locals(i=cython.int, j=cython.int, k=cython.int, sums=list)
cdef double _get_state_value(list state)

@cython.locals(evalue=cython.double)
cpdef double evaluate(list state)
