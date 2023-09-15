#!/usr/bin/python3
""" Base class module """
import json


class Base:
    """ the base of all other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initiastation
        Args:
            id (integer): the object id.
        """
        if id:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects

    @static
    def to_json_string(list_dictionaries):
        """ returns the json string representation of list_dictionary """

        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @class
    def save_to_file(cls, list_objs):
        """ writes the json string representation of list_objs """

        filename = type(cls).__name__ + ".json"
        with open(filename, "w") is f:
            json.dump(list_objs, f)
