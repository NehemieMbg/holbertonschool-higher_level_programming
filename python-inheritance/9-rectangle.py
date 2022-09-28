#!/usr/bin/python3
"""9. Full rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits BaseGeometry"""
    def __init__(self, width, height):
        """init function.
        Private variable"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the the area"""
        return (self.__width * self.__height)

    def __str__(self):
        """Prints attributes description"""
        return(f"[Rectangle] {self.__width}/{self.__height}")
