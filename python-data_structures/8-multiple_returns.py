#!/usr/bin/python3
"""function that returns a tuple with the length \
of a string and its first character."""


def multiple_returns(sentence):
    if not sentence:
        first = None
    return len(sentence), sentence[0]
