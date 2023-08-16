#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for line in range(len(matrix)):
        for raw in range(len(matrix[line])):
            new[line][raw] = matrix[line][raw] ** 2
    return new
