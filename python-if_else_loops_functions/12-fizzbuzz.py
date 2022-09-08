#!/bin/usr/python3
# prints the numbers from 1 to 100


def fizzbuzz():
    for number in range(1, 101):
        if number % 5 == 0 and number % 3 == 0:
            print("FizzBuzz", end=' ')
        elif number % 5 == 0:
            print("Buzz", end=' ')
        elif number % 3 == 0:
            print("Fizz", end=' ')
        else:
            print(number, end=' ')
