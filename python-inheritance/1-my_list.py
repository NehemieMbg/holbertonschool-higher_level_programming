#!/usr/bin/python3
"""Module 1 - My list"""


class MyList(list):
    """Anthony"""

    def print_sorted(self):
        """print the 'list', but sorted
        ascending sort we mean"""
        print(sorted(self))
