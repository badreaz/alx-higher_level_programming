#!/usr/bin/python3
""" This module defines 'matrix_divided' """


def matrix_divided(matrix, div):
    """ divides all elements of a matrix """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    msize = len(matrix[0])
    result = []
    for row in matrix:
        if len(row) != msize:
            raise TypeError("Each row of the matrix must have the same size")
        new = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new.append(round(element / div, 2))
        result.append(new)
    return result
