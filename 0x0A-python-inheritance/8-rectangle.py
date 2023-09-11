#!/usr/bin/python3
""" Rectangle class module """


class Rectangle(BaseGeometry):
    """ class that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ instantiation
        Args:
            width: rectangle width.
            height: rectangle height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height
