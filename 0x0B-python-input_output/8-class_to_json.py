#!/usr/bin/python3
""" class_to_json definition module """


def class_to_json(obj):
    """ returns the dictionary description of an object """
    return obj.__dict__
