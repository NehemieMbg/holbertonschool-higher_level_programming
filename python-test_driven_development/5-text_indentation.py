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
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Prints 2 new lines after a punctuation
    newText = text.replace(".", ".\n\n")
    newText = newText.replace("?", "?\n\n")
    newText = newText.replace(":", ":\n\n")
    # Splits line when it encounters "\n"
    parser = newText.splitlines(True)
    print(parser)
    # Declaring a new list
    newList = []
    # If index is a new line a new line is push to the newList
    for index in parser:
        if index == "\n":
            newList.append("\n")
    # else it pushes index to newlist with
    # while removing the first space before the word
        else:
            newList.append(index.lstrip())
    # Joins the list back to a string
    print("".join(newList), end="")
