#!/usr/bin/python3
# Prints all number from 0 to 98
for i in range(99):
    if i > 0 and i < 99:
        print(', ', end='')
    print('0{}'.format(i) if i < 10 else '{}'.format(i), end='')
