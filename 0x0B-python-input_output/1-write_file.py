#!/usr/bin/python3
""" write_file definition module """


def write_file(filename="", text=""):
    """ writes a string to a text file and
    returns charcter written count """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
