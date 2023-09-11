#!/usr/bin/python3
""" inherits_from definition module """


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of
    a class that inherited from the specified class;
    othrwise False """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
