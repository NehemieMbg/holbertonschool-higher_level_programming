#!/usr/bin/python3
"""
Python test driven development with text file(2-matrix_divided.txt)
"""


def matrix_divided(matrix, div):
    """
    Function that devides all elements of a matrix
    Takes: integers or floats as arguments
    """
    # Error Message stock in a varaibale
    messageError = "matrix must be a matrix (list of lists) of integers/floats"
    # Check if matrix exist
    if not matrix:
        raise TypeError(messageError)
    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError(messageError)
    # Check if the lists in the matrix are lists
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(messageError)
        # Check if the elements of the lists are int or float
        for value in lists:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError(messageError)
    # Check for the length of the list
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(messageError)
    # Check if the value in div is not an int or a float
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if not all(len(lists) == len(matrix[0]) for list in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Return the value in the lists divided by div
    return [[round(value / div, 2) for value in lists] for lists in matrix]
