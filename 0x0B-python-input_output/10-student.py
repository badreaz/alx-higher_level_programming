#!/usr/bin/python3
""" Student class module """


class Student():
    """ class that defines a student """

    def __init__(self, first_name, last_name, age):
        """ instantation
        Args:
            first_name: student first name.
            last_name: student last name
            age: student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation """
        if type(attrs) is list and
        all(type(attr) is str for attr in attrs):
            return dict(self.__dict__[attr] for attr in attrs if hasattr(self, attr))
        return self.__dict__
