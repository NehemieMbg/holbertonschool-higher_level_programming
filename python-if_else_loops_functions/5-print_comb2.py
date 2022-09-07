#!/usr/bin/python3
# Prints all number from 0 to 98
for i in range(100):
    if i > 0 and i < 100:
        print(', ', end='')
    print('0{}'.format(i) if i < 10 else '{}'.format(i), end='')
