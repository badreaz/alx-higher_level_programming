#!/usr/bin/python3
""" Square class module """
Rectangle = __import__("rectangle").Rectangle


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

        return "[Square] [{}] {}/{} - {}".format(self.id, self.x, self.y, self.width)

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

        if args is not None:
            n = 1
            for arg in args:
                if n == 1:
                    self.id = arg
                elif n == 2:
                    self.size = arg
                elif n == 3:
                    self.x
                elif n == 4:
                    self.y
                n++
        else:
            for k, v in kwargs.iteritems():
                self.k = v
