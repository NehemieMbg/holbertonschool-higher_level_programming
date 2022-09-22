#!/usr/bin/python3
"""
Prints the first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Defines a function.
    first_name: Takes the first name as an argument
    last_name: Takes the last name as an argument
    Arguments must be string type
    """
    # Check if thr first name is a string
    if type(first_name) is not str:
        """ Check if the fist name is a string """
        raise TypeError("{:s} must be a string".format("first_name"))
    # Check if the last name is a string
    if type(last_name) is not str:
        """ Check if the last name is a string """
        raise TypeError("{:s} must be a string".format("last_name"))
    # If the first and last name are strings
    else:
        """ Else printsMy name is <first name> <last name> """
        print("My name is {:s} {:s}".format(first_name, last_name))
