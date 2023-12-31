#!/usr/bin/python3
""" Rectangle class module """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
        self.__width = width
        self.__height = height

    def __str__(self):
        """ print the width and height """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ find area of a rectangle """
        return self.__width * self.__height
