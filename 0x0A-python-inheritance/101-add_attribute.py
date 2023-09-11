#!/usr/bin/python3
""" add_attribute definition module """


def add_attribute(obj, name, value):
    """ add a new attribut to an object """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
