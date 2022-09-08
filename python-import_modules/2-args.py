#!/usr/bin/python3
# Prints the number of and the list of its arguments
from sys import argv


def print_argument():
    print('{} argument'.format(len(argv) - 1), end='')
    if len(argv) == 1:
        print('.', end='')
    elif len(argv) == 2:
        print(':', end='')
    elif len(argv) > 2:
        print('s:', end='')
    print('')

    for index in range(1, len(argv)):
        print('{}: {}'.format(index, argv[index]))


if __name__ == "__main__":
    print_argument()
