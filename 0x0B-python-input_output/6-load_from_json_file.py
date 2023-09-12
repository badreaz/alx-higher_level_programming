#!/usr/bin/python3
""" load_from_json_file definition module """
import json


def load_from_json_file(filename):
    """ creates an object from json file """
    with open(filename, "r") as f:
        return json.load(f)
