#!/usr/bin/python3
# rints the last digit of a number
def print_last_digit(number):
    if number < 0:
        number *= -1
    print(number %10, end='')
    return number %10
