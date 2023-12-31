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
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__position = position
        self.__size = size

    @property
    def size(self):
        """ retrieve size value """
        return self.__size

    @property
    def position(self):
        """ retrive position value """
        return self.__position

    @size.setter
    def size(self, value):
        """ set a value to __size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """ set a value to __position """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(x, int) for x in value) or
                not all(x >= 0 for x in value)):
            raise TypeError("position must be a tuble of 2 positive integers")

        self.__position = value

    def area(self):
        """ count the area of a square """
        return self.__size ** 2

    def my_print(self):
        """ print square using '#' """
        if self.__size == 0:
            print()
            return
        print('\n' * self.__position[1], end="")
        for i in range(self.__size):
            print(' ' * self.__position[0], end="")
            print('#' * self.__size)
