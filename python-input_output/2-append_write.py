#!/usr/bin/python3
"""2. Append to a file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file"""
    with open(filename, mode="a", encoding="UTF8") as f:
        f.write(text)
        return(len(text))
