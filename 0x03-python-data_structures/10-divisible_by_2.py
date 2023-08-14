#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        ret_list = []
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                ret_list[i] = True
            else:
                ret_list[i] = False
        return ret_list
    else:
        return None
