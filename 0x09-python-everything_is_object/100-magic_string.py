#!/usr/bin/python3
def magic_string():
    magic_string.num = getattr(magic_string, 'num', -1) + 1
    return "BestSchool" + ", BestSchool" * magic_string.num
