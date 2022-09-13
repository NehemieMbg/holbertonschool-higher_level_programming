#!/usr/bin/python3
# removes all characters c and C from a string

def no_c(my_string):
    newString = ""
    for string in (my_string):
        if string != 'c' and string != 'C':
            newString += string
    return newString
