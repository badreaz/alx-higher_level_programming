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

    def to_json(self):
        """ retrieves a dictionary representation """
        return self.__dict__
