#!/usr/bin/python3
""" Defines a square """


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """returns the current square area"""
    def area(self):
        return int(self.__size ** 2)
