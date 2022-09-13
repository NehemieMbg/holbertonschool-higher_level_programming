#!/usr/bin/python3
# Function that prints a matrix of integers.


def print_matrix_integer(matrix=[[]]):
    for index in matrix:
        print(" ".join('{:d}'.format(j) for j in index))
