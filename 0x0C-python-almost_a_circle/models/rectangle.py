#!/usr/bin/python3
""" Rectangle class module """
Base = __import__("base").Base


class Rectangle(Base):
    """ class that defines a rectangle
    - inherits from the class Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiation
        Args:
            width: rectangle width.
            height: rectangle height.
            x: x
            y: y
            id: rectangle id.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """ return instance data """

        data = "[Rectangle] ({}) {}/{}".format(self.id, self.__x, self.__y)
        data += " - {}/{}".format(self.__width, self.__height)
        return data

    @property
    def width(self):
        """ property to retrieve width """

        return self.__width

    @width.setter
    def width(self, value):
        """ property setter to set width """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ property to retrieve height """

        return self.__height

    @height.setter
    def height(self, value):
        """ property setter to heigth """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ property to retrieve x """

        return self.__x

    @x.setter
    def x(self, value):
        """ property setter to set x """

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ property to retrieve y """

        return self.__y

    @y.setter
    def y(self, value):
        """ property setter to set y """

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area value of the instance """

        return self.__width * self.__height

    def display(self):
        """ prits the instance with '#' """

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x, end="")
            print('#' * self.__width)

    def update(self, *args, **kwargs):
        """ assigns an argument to each sttribute """

        if args is not None:
            n = 1
            for arg in args:
                if n == 1:
                    self.id = arg
                elif n == 2:
                    self.width = arg
                elif n == 3:
                    self.height = arg
                elif n == 4:
                    self.x = arg
                elif n == 5:
                    self.y = arg
                n++
        else:
            for k, v in kwargs.iteritems():
                self.k = v
