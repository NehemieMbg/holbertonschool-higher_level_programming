#!/usr/bin/python3
# Returns Roman numbers to Integer


def roman_to_int(roman_string):
    # Dictionary for the roman number
    lookup = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    # If roman_string is not a string or doesn't exist
    if not isinstance(roman_string, str) or None:
        return 0
    # num = the length of roman_string
    num = len(roman_string)
    i = num - 1
    output = 0
    # Loop starting from the end
    while i >= 0:
        # If the roman number at the index is bigger than
        # the next index does a subtraction
        if i < num - 1 and lookup[roman_string[i]]\
                < lookup[roman_string[i + 1]]:
            output -= lookup[roman_string[i]]
        # Else does an addition
        else:
            output += lookup[roman_string[i]]
        # Decrementation for looping in reverse
        i -= 1
        # Return the Roman number to integers number
    return output
