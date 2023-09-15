#!/usr/bin/python3
""" Base class module """


class Base:
    """ the base of all other classes """
    __nb_objects = 0

    def __init__(self, id=name):
        """ initiastation
        Args:
            id (integer): the object id.
        """
        if id:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
