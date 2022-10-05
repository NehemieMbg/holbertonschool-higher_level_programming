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

    def update(self, *args, **kwargs):
        """Assings arguments to each attribute"""
        if args:
            for arg, ele in enumerate(args):
                if arg == 0:
                    self.id = ele
                if arg == 1:
                    self.size = ele
                if arg == 2:
                    self.x = ele
                if arg == 3:
                    self.y = ele
        else:
            # Assigns a key/value argument to attributes
            for key, value in kwargs.items():
                if "id" == key:
                    self.id = value
                if "size" == key:
                    self.size = value
                if "x" == key:
                    self.x = value
                if "y" == key:
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary reepresentation of a square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
