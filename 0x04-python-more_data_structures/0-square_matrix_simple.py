#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for line in matrix:
        new.append(num ** 2 for num in line)
    return new
