#!/usr/bin/python3
# Defines a square based on 3-square.py
"""
Defines a class Square
Takes only integers as input
    """


class Square:
    """
    Class Square
        """
    def __init__(self, size=0):
        """
        Initializing
        Attributes:
            Private instance size
            """
        self.__size = size

    @property
    def size(self):
        """
        Getter method
        Retrives the property
            """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method
        Sets the property
            """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Public instance method
        Returns the current square area
            """
        return int(self.__size ** 2)
