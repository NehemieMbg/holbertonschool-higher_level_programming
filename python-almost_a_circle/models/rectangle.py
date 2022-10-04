#!/usr/bin/python3
"""2. First Rectangle"""
# Import Base from models/base
from models.base import Base


class Rectangle(Base):
    """Initiate an object
    Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        # Calls the super class with id
        super().__init__(id)

    @property
    def width(self):
        """Getter: gets the width's value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter: sets the width's value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter: gets the height's value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter: sets the height's value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter: gets x's value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter: sets x's value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter: gets y's value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter: sets y's value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
