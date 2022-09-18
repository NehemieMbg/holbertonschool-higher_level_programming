#!/usr/bin/python3
# Prints an integer with "{:d}".format()


def safe_print_integer(value):
    # Will try to print an integer and return true
    # if value is an integer
    try:
        print("{:d}".format(value))
        return True
    # Return false otherwise
    except:
        return False
