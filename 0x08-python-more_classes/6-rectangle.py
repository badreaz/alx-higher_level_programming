#!/usr/bin/python3
""" Rectangle class module """


class Rectangle:
    """ empty class that defines  rectangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """  instantiation
        Args:
            width: rectangle width.
            height: rectangle height.
        """

        number_of_instances += 1
        self.width = width
        self.height = height

    def __str__(self):
        """ print the rectangle with the character '#' """

        rectangle = ""
        if not self.__width or not self.__height:
            return rectangle
        for i in range(self.__height):
            rectangle += "#" * self.__width
            if i is not self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """ return a string representation of the rectangle """

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ print a message when an instance id deleted """

        number_of_instances -= 1
        print("Bye rectangle...")

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
