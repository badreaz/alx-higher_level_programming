#!/usr/bin/python3
""" pascal_triange definition module """


def pascal_triangle(n):
    """ return's a list of lists of integers representing
    the pascal's triangle of n """
    my_list = []
    if n <= 0:
        return my_list
    for i in range(0, n):
        if i == 0:
            my_list.append([1])
        else:
            sub_list = []
            sub_list = [1]
            for j in range(1, len(my_list[i - 1])):
                num = my_list[i - 1][j - 1] + my_list[i - 1][j]
                sub_list.append(num)
            sub_list.append(1)
            my_list.append(sub_list)
    return my_list
