#!/usr/bin/python3
"""1. Write to a file"""


def write_file(filename="", text=""):
    """Writes a string to a text file"""
    with open(filename, mode="w", encoding="UTF8") as f:
        f.write("text")
        return(len(text))
