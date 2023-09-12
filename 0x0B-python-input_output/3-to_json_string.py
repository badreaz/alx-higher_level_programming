#!/usr/bin/python3
""" to_json_string definition module """
import json


def to_json_string(my_obj):
    """ returns the json representation of an object """
    return json.dumps(my_obj)
