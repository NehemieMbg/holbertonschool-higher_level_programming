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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializing
        Attributes:
            Private instance size
            """
        self.size = size
        self.position = position

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter"""
        if not isinstance(value, tuple) or len(value) != 2\
            or not isinstance(value[0], int) or not\
                isinstance(value[1], int) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Public instance method
        Returns the current square area
            """
        return int(self.__size ** 2)

    def my_print(self):
        """
        Function:
        Prints the square with
        # character times size
            """
        if self.__size == 0:
            prints("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join(" " * self.__position[0] +
                            "#" * self.__size for rows in range(self.__size)))
