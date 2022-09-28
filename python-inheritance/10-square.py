#!/usr/bin/python3
"""10. Square #1"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that inherits from Rectangle"""
    def __init__(self, size):
        """Function that takes in an integer,
        with a private variable"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
