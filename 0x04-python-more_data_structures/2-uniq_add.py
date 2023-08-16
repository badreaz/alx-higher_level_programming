#!/usr/bin/python3
def uniq_add(my_list=[]):
    old = []
    result = 0
    for num in my_list:
        if num not in old:
            result += num
        old.append(num)
    return result
