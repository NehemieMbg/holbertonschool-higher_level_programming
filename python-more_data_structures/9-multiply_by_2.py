#!/usr/bin/python3
# Returns a new dictionary with all values multiplied by 2


def multiply_by_2(a_dictionary):
    return {key: a_dictionary[key] * 2 for key in a_dictionary}
