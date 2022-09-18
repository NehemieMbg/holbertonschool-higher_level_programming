#!/usr/bin/python3


# Function that divies 2 integers and prints the result.
def safe_print_division(a, b):
    # If result a can be devided by b
    try:
        result = a / b
    # Expetion if a value is devided by zero
    except ZeroDivisionError:
        result = None
    # Prints the return value no matter what
    finally:
        print("Inside result: {}".format(result))
    # returns the result
    return result
