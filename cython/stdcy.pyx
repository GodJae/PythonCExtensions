from libcpp.vector cimport vector

cdef extern from "std.h":
    double standardDeviation(vector[double])

def standard_dev(lst):
    # This pre-conversion has some performance improvements.
    cdef vector[double] v = lst

    return standardDeviation(v)
