#!/usr/bin/python3
""". Base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSONS string representation"""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
