#!/usr/bin/python3
"""Define Square Class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of Square as a Module
    """


    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size of the Square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size of the Square
        """
        self.width = value
        self.height = value


    def __str__(self):
        """String representation of the Square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """Update method for the Square
        """
        if len(args):
            for m, arg in enumerate(args):
                if m == 0:
                    self.id = arg
                elif m == 1:
                    self.size = arg
                elif m == 2:
                    self.x = arg
                elif m == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)


    def to_dictionary(self):
        """Return a dictionary representation of the Square
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
