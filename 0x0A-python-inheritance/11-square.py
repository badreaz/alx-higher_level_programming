#!/usr/bin/python3
""" Square class module """

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ class that inherits from Rectangle """

    def __init__(self, size):
        """ instatiation
        Args:
            size: square size.
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """ print square description """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """ return the area of square """
        return self.__size ** 2
