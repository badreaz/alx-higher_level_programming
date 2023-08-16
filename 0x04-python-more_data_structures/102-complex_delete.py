#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = dict(a_dictionary)
    for k, v in tmp.items():
        if v == value:
            a_dictionary.pop(k, None)
    return a_dictionary
