#!/usr/bin/python3
""". Base class"""

class Base:
    """initiate an Object"""
    # private class attribute
    __nb_objects = 0
    def __init__(self, id=None):
        """assign to a public instance attribute id"""
        # if id exist id is assign with a value
        # that already exist in id
        if id is not None:
            self.id = id
        # else __nb_objects is incremented and assigned
        # to the public instance attribute id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
