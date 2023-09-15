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

    @static
    def from_json_string(json_string):
        """ returns the list of json strin representation json_string """

        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @class
    def create(cls, **dictionary):
        """ returns an instance with all attributes set """

        dummy = cls(0, 0, 0)
        return dummy.update(**dictionary)
