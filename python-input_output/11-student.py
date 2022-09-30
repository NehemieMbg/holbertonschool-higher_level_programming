#!/usr/bin/python3
"""11. Student to disk and reload"""


class Student:
    """Initialize a new object"""
    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of a student"""
        # check the type of attrs
        if isinstance(attrs, list):
            # create a new dictionary
            dic = {}
            for attr in attrs:
                # check if the attribute exist
                if hasattr(self, attr):
                    # gives the attribute to a new dictionary
                    dic[attr] = getattr(self, attr)
            # returns the dictionary
            return dic
        else:
            # else returns the full dictionary obj
            return vars(self)

    def reload_from_json(self, json):
        """Replaces attribute of the Student instance"""
        for key, value in json.items():
            # Sets or replace an attribute
            setattr(self, key, value)
