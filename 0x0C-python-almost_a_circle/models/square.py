#!/usr/bin/python3
""" Square class module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class that defines a square
    - inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ instantiation
        Args:
            size: square size.
            x: x-axis.
            y: y-axis.
            id: instance id.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return square data """

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ property to retrieve size """

        return self.width

    @size.setter
    def size(self, value):
        """ property setter to set size """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update the class attributes """

        if args:
            attr = ['id', 'size', 'x', 'y']
            for n, arg in enumerate(args):
                setattr(self, attr[n], arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ returns dictionary representation of a square """

        return {'x': self.x, 'y': self.y, 'id': self.id,
                                'size': self.size}
