#!/usr/bin/python3
# Prints all number from 0 to 98
for i in range(99):
    if i < 10:
        print(0, end='')
    elif i == 98:
        print(98)
    print('{}, '.format(i), end='')
