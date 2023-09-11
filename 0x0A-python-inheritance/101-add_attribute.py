#!/usr/bin/python3
""" add_attribute definition module """


def add_attribute(obj, name, value):
    """ add a new attribut to an object """
    if not setattr(obj, name, value):
        raise TypeError("can't add new attribute")
