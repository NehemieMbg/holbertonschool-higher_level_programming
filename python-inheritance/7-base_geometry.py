#!/usr/bin/python3
"""7. Integer validator"""


class BaseGeometry:
    """Defines a class"""
    def area(self):
        """Raises an exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        # check if value is the right type
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        # check if value is greater than 0
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
