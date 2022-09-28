#!/usr/bin/python3
"""8. Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits BaseGeometry"""
    def __init__(self, width, height):
        """init function.
        Private variable"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.height = height
