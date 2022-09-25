#!/usr/bin/python3
"""2. Area and Peirimeter"""


class Rectangle:
    """
    Defines a class Rectangle:
        Private Attribure:
            width, height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter: Gets the width Value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter: Sets the width Value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter: Gets the height Value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter: Sets the height Value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return ((self.width) * (self.height))

    def perimeter(self):
        """Returns the rectangle peirimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
