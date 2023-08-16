#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for line in matrix:
        for raw in line:
            new.append(raw ** 2)
    return new
