#!/usr/bin/python3
"""10. Student to JSON with filter"""


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
