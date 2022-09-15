#!/usr/bin/python3
# Returns a new dictionary with all values multiplied by 2


def multiply_by_2(a_dictionary):
    newDic = a_dictionary
    for key in newDic:
        newDic[key] = newDic[key] * 2
    return newDic
