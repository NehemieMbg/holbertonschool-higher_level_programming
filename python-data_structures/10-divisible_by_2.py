#!/usr/bin/python3
# Function that finds all multiples of 2 in a list.


def divisible_by_2(my_list=[]):
    newList = my_list.copy()
    for num in range(len(my_list)):
        if my_list[num] % 2 == 0:
            newList[num] = True
        else:
            newList[num] = False
    return newList
