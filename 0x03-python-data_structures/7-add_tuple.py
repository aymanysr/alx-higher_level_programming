#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    elem_a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    elem_a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    elem_b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    elem_b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (elem_a1 + elem_b1, elem_a2 + elem_b2)
