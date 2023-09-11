#!/usr/bin/python3
""" MyInt class module """


class MyInt(int):
    """ class that inherits from int """

    def __init__(self, value):
        """ instantiation
        Args:
            value: number.
        """
        self.value = value

    def __eq__(self, other):
        """ make == work as != """
        return self.value != other

    def __ne__(self, other):
        """ make != work as == """
        return self.value == other
