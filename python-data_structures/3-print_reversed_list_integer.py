#!/usr/bin/python3
# Prints all integers of a list, in reverse order


def print_reversed_list_integer(my_list=[]):
    if my_list:
        for index in range(len(my_list)-1, -1, -1):
            print('{:d}'.format(my_list[index]))
