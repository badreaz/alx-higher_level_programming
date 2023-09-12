#!/usr/bin/python3
""" from_json_string definition module """
import json


def from_json_string(my_str):
    """ returns an object represented by json string """
    return json.loads(my_str)
