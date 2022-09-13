#!/usr/bin/python3
# Replaces an element in a list at a specific position


def new_in_list(my_list, idx, element):
    if idx < 0 and idx > len(my_list):
        return my_list

    newList = my_list
    newList[idx] = element
    return my_list
