#!/usr/bin/python3
# Defines a square based on 3-square.py

""" New blueprint Square"""


class Square:
    def __init__(self, size=0):
        self.__size = size

    """ Getter that reeturn the private variable"""
    @property
    def size(self):
        return self.__size

    """ Sets the value of a property """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    """ Returns the current square area """
    def area(self):
        return int(self.__size ** 2)
