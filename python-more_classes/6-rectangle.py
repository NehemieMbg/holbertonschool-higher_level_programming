#!/usr/bin/python3
"""3. String representation"""


class Rectangle:
    """
    Defines a class Rectangle:
        Private Attribure:
            width, height
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        # Prints the total + 1 rectangle instances
        Rectangle.number_of_instances += 1

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
        """Returns the Rectangle area"""
        return ((self.width) * (self.height))

    def perimeter(self):
        """Returns the Rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        """Prints the rectangle with the character #"""
        if self.width != 0 and self.height != 0:
            return ("\n".join("#" * self.width for i in range(self.height)))
        else:
            return ""

    def __repr__(self):
        """Returns a string represation fo the rectangle"""
        if self.width != 0 and self.height != 0:
            return ("Rectangle({}, {})".format(self.width, self.height))
        else:
            return ""

    def __del__(self):
        """
        Prints a slute a message when an instace of
        rectangle is deleted.
        """
        print("Bye rectangle...")
        # Prints the total - 1 rectangle instances
        Rectangle.number_of_instances -= 1
