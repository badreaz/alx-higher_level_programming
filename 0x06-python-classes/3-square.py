#!/usr/bin/python3
""" Square class module """


class Square:
    """ class that definess square

    Args:
        size (int): square size.
    Raises:
        TypeError: if size is not integer.
        ValueError: if size is less than 0.

    Attributes:
        size (int): square size.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ count the area of a square """
        return self.__size ** 2
