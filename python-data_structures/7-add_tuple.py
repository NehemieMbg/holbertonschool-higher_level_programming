#!/usr/bin/python3
# Function that adds 2 tuples.


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2: tuple_a += 0, 0
    if len(tuple_b) < 2: tuple_b += 0, 0
    result = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return result
