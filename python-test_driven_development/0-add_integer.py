#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Define a function that adds two integers
    """
    if type(a) is int or type(a) is float:
        try:
            a = int(a)
        except:
            raise TypeError("a must be an integer")
    else:
        raise TypeError("a must be an integer")

    if type(b) is int or type(b) is not float:
        try:
            b = int(b)
        except:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
    return a + b
