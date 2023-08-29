#!/usr/bin/python3
""" Square class module """


class Square:
    """Square class

    Args:
        size (int): square size.
    Raises:
        TypeError: if size is not integer.
        ValueError: if size is less than 0.

    Attributes:
        size (int): square size.
    """
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
