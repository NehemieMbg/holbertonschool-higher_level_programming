#!/usr/bin/python3
# function that finds the biggest integer of a list.


def max_integer(my_list=[]):
    if my_list:
        my_list.sort()
        number = len(my_list) - 1
        return my_list[number]
    return None
