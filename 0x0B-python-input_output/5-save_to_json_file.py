#!/usr/bin/python3
""" save_to_json_file definition module """
import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file, using a json representation """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
