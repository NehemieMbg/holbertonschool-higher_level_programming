#!/usr/bin/python3
"""
Prints a text with 2 lines after
each of these characters: ".", "?",":"
"""


def text_indentation(text):
    """
    Defines a function.
    Takes a string as an argument
    """
    # Check if the text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Prints 2 new lines after a punctuation
    for char in text:
        if char == " ":
            continue   
        if char == "." or char == "?" or char == ":":
            print(f"{char}\n")
        else:
            print(char, end="")
