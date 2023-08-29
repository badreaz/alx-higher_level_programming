#!/usr/bin/python3
""" bytecode task """


class MagicClass:
    """ magicclass """
    def __init__(self, radius=0):
        """ initiation """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ find the area """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ find circumference """
        return math.pi * 2 * self.__radius
