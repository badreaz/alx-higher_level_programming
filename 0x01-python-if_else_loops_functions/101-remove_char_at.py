#!/usr/bin/python3
def remove_char_at(str, n):
    copy = str[:n] + [n + 1 : ]
    return copy
