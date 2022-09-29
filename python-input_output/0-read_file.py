#!/usr/bin/python3
"""0. Read file"""


def read_file(filename=""):
    """Function that reads a text file"""
    with open(filename, encoding="UTF8") as f:
        for lines in f:
            print(lines, end="")
