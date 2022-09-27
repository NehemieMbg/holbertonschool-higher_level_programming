#!/usr/bin/python3
"""4.Only sub class of"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance
    of a class that inherited from a class"""
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
