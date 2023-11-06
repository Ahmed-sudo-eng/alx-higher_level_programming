#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        a_0, a_1 = tuple_a[0], tuple_a[1]
    elif len(tuple_a) == 1:
        a_0, a_1 = tuple_a[0], 0
    elif len(tuple_a) == 0:
        a_0, a_1 = 0, 0

    if len(tuple_b) >= 2:
        b_0, b_1 = tuple_b[0], tuple_b[1]
    elif len(tuple_b) == 1:
        b_0, b_1 = tuple_b[0], 0
    elif len(tuple_b) == 0:
        b_0, b_1 = 0, 0

    c_0 = a_0 + b_0
    c_1 = a_1 + b_1
    tuple_c = (c_0, c_1)
    return tuple_c
