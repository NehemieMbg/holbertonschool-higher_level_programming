#!/usr/bin/python3


def roman_to_int(roman_string):
    lookup = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    if not roman_string or None:
        return 0

    num = len(roman_string)
    i = num - 1
    output = 0

    while i >= 0:
        if i < num - 1 and lookup[roman_string[i]]\
                < lookup[roman_string[i + 1]]:
            output -= lookup[roman_string[i]]
        else:
            output += lookup[roman_string[i]]
        i -= 1
    return output
