#!/usr/bin/python3
# Prints the first x elements of a list and only integers


def safe_print_list_integers(my_list=[], x=0):
    # Counts how many elements are printed
    count = 0
    # Loop to print elements of the list and count + 1 for each element
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        # ValueError: Raised when a function gets an argument of
        # correct type but improper value.
        # TypeError: Raised when a function or operation is
        # applied to an object of incorrect type.
        except (ValueError, TypeError):
            continue
    print()
    # Returns the number of elements printed
    return count
