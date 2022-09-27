#!/usr/bin/python3
"""1.My list"""


class MyList(list):
    """Inherits list"""

    def print_sorted(self):
        """Function that print a sorted list"""
        print(sorted(self))
