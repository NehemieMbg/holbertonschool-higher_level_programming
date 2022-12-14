#!/usr/bin/python3
# prints x elements of a list


def safe_print_list(my_list=[], x=0):
    jdx = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            jdx += 1
        except IndexError:
            break
    print()
    return jdx
