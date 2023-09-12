#!/usr/bin/python3
""" adds all arguments to a python list, then save them to a file """
import json
import sys
import os.path
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
my_obj = []
if os.path.isfile(filename):
    my_obj = load_from_json_file(filename)
for i in range(1, len(sys.argv)):
    my_obj.append(sys.argv[i])
save_to_json_file(my_obj, filename)
