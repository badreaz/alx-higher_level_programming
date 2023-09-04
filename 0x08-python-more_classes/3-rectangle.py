#!/usr/bin/python3
""" Rectangle class module """


class Rectangle:
    """ empty class that defines  rectangle """

    def __init__(self, width=0, height=0):
        """  instantiation
        Args:
            width: rectangle width.
            height: rectangle height.
        """

        self.width = width
        self.height = height

    def __str__(self):
        """ print the rectangle with the character '#' """

        rectangle = ""
        if not self.__width or not self.__height:
            return ""
        for i in range(self.__height):
            rectangle += '#' * self.__width
            if i + 1 == self.__height:
                rectangle += '\n'
        return rectangle

    @property
    def width(self):
        """ property to retrieve width """

        return self.__width

    @width.setter
    def width(self, value):
        """ property setter to set width """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ property to retrieve height """

        return self.__height

    @height.setter
    def height(self, value):
        """ property setter to set height """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ method that returns the rectangle area """

        return self.__width * self.__height

    def perimeter(self):
        """ method that returns the rectangle perimeter """

        if not self.__width or not self.__height:
            return 0

        return self.__width * 2 + self.__height * 2
