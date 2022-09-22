#!/usr/bin/python3
"""
Function that prints the square
with the character #
"""


def print_square(size):
    """
    Defines a function
    Takes an integer as an argument
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    # Check if size is greater than 0
    if size < 0:
        raise ValueError("size must be >= 0")
    # Check if size is not a float
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        print("", end="")
    # Prints the square with the character #
    else:
        print("\n".join("#"*size for rows in range(size)))
