#!/usr/bin/python3
def add_tuple(tuple_a=(), tuble_b=()):
    new = ()
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    new = (tuple_a[0] + tuple_b[0],
            tuple_a[1] + tuplle_b[1])
    return new
