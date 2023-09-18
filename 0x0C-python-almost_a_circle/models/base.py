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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the json string representation of list_dictionary """

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the json string representation of list_objs """

        if not list_objs:
            return
        filename = cls.__name__ + ".json"
        with open(filename, "w", "utf-8") as f:
            dic = []
            for obj in list_objs:
                dic.append(obj.to_dictionary())
            f.write(Base.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of json strin representation json_string """

        if json_string is None or not len(json_string):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes set """

        dummy = cls(0, 0)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instance """

        filename = cls.__name__ + ".json"
        with open(filename, "r") as f:
            inst_list = []
            objs = cls.from_json_string(f.read().replace('\n', '')
            for new in objs:
                inst_list.append(cls.create(**new))
            return inst_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serialize an object to csv """

        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if cls.__name__ == "Rectangle":
                f.write("id,width,height,x,y\n")
                for obj in list_objs:
                    id = obj.id
                    w = obj.width
                    h = obj.height
                    x = obj.x
                    y = obj.y
                    f.write("{},{},{},{},{}\n".format(id, w, h, x, y))
            else:
                f.write("id,size,x,y\n")
                for obj in list_obj:
                    id = obj.id
                    s = obj.size
                    x = obj.x
                    y = obj.y
                    f.write("{},{},{},{}\n".format(id, s, x, y))

    @classmethod
    def load_from_file_csv(cls):
        """ deserialize an csv to an object """

        filename = cls.__name__ + ".csv"
        with open(filename, "r") as f:
            list_objs = []
            form = f.readline().replace('\n', '').split(',')
            for line in f:
                dictionary = dict(zip(form, int(line.replace('\n', '').split(','))))
                obj = cls.create(**dictionary)
                list_objs.append(obj)
            return list_objs
