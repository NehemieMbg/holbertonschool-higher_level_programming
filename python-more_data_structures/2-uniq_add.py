#!/usr/bin/python3
# Adds all unique integers in a list


def uniq_add(my_list=[]):
    result = sum(set(my_list))
    return result
