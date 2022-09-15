#!/usr/bin/python3
# Computes the square value of all integers of a matrix


def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(lambda idx:idx ** 2, num)) for num in matrix]
    return new_matrix
