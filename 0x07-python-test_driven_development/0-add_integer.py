#!/usr/bin/python3
def add_integer(a, b=98):
    """ add 2 integers """
    if a is None or not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a + b)
