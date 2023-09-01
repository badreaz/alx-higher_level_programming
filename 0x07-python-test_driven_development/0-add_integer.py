#!/usr/bin/python3
def add_integer(a, b=98):
    """ add 2 integers """
    if type(a) is not int or float:
        raise TypeError("a must be an integer")
    elif type(b) is not int or float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
