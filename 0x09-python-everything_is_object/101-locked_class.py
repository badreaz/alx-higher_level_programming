#!/usr/bin/python3
""" LockedClass class module """


class LockedClass:
    """ class with no class or object attribute """

    __slots__ = ['firs_name']

    def __init__(self, name):
        """ first define """

        self.first_name = name
