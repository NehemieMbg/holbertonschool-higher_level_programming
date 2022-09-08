#!/usr/bin/python3
# prints a string in uppercase followed by a new line
def uppercase(str):
    for character in str:
        if ord('a') <= ord(character) <= ord('z'):
            character = chr(ord(character) - (ord('a') - ord('A')))
        print("{}".format(character), end='')
    print("")
