#!/usr/bin/python3
"""Function that return True if
the object is an instance of a class"""


def is_same_class(obj, a_class):
    """Check if instance of a class"""
    if type(obj) is a_class:
        return True
    else:
        return False
