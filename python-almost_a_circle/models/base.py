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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs"""
        fileName = cls.__name__ + ".json"
        newList = []
        if list_objs is not None:
            for i in list_objs:
                newList.append(cls.to_dictionary(i))
        with open(fileName, mode="w+") as f:
            f.write(cls.to_json_string(newList))
