#!/usr/bin/python3
# Returns a list wit all values multiplied by a number


def multiply_list_map(my_list=[], number=0):
    return list(map(lambda a: a * number, my_list))
