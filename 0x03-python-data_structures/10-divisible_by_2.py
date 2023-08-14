#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        return [not x % 2 for x in my_list]
    else:
        return None
