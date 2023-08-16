#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    if not a_dictionary:
        return None
    for k, v in a_dictionary.items():
        if v > best:
            best = v
            key = k
    return key
