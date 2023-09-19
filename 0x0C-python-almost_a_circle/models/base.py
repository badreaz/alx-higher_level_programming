#!/usr/bin/python3
""" Base class module """
import json
import csv
import turtle


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

        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            dic = []
            if list_objs:
                for obj in list_objs:
                    dic.append(obj.to_dictionary())
            f.write(cls.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of json strin representation json_string """

        if not json_string or not len(json_string):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes set """

        name = cls.__name__
        if name == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instance """

        filename = cls.__name__ + ".json"
        inst_list = []
        try:
            with open(filename, "r") as f:
                objs = cls.from_json_string(f.read())
                for new in objs:
                    inst_list.append(cls.create(**new))
            return inst_list
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serialize an object to csv """

        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if not list_objs:
                return
            keys = list(list_objs[0].__dict__.keys())
            f.write(','.join(keys) + '\n')
            for obj in list_objs:
                values = list(obj.__dict__.values())
                f.write(','.joine(values) + '\n')

    @classmethod
    def load_from_file_csv(cls):
        """ deserialize an csv to an object """

        filename = cls.__name__ + ".csv"
        list_objs = []
        try:
            with open(filename, "r") as f:
                csv_r = csv.DictReader(f)
                for line in csv_r:
                    for k, v in line.items():
                        line[k] = int(v)
                    obj = cls.create(**line)
                    list_objs.append(obj)
            return list_objs
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_square):
        """ draws Rectangles and Squarea """

        t = turtle.Turtle()
        list_shapes = list_rectangles + list_square
        for shape in list_shapes:
            t.penup()
            t.goto(shape.x, shape.y)
            t.pendown()
            for _ in range(2):
                t.forward(shape.width)
                t.right(90)
                t.forward(shape.height)
                t.right(90)
        turtle.done()
