#!/usr/bin/python3
""" append_after definition module """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file after each
    line containing a specific string """
    with open(filename, "r") as f:
        of = f.readlines()

    with open(filename, "w") as f:
        for line in of:
            f.write(line)
            if search_string in line:
                f.write(new_string)
