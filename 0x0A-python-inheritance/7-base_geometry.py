#!/usr/bin/python3
""" BaseGeometry class module """


class BaseGeometry:
    """ class implementation """

    def area(self):
        """ find area
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value
        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            TypeError("{} must be an integer".format(name))
        elif value < 0:
            ValueError("{} must be greater than 0".format(name))
