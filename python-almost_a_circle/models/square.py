#!/usr/bin/python3
"""Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Initiate an object
    Inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter: gets the value"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter: sets the value"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
