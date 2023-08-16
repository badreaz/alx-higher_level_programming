#!/usr/bin/python3
def only_deff_elements(set_1, set_2):
    deff = []
    for element in set_1:
        if element not in set_2:
            deff.append(element)
    return deff
