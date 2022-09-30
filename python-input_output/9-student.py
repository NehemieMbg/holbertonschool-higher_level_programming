#!/usr/bin/python3
"""9. Student to JSON"""


class Student:
    """Initialize a new object"""
    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation"""
        return vars(self)
