#!/usr/bin/python3
""" matrix_mul definition module """


def matrix_mul(m_a, m_b):
    """ multiplies 2 matrices """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif not all(isinstance(r, list) for r in m_a):
        raise TypeError("m_a must be a list of lists")
    elif not all(isinstance(r, list) for r in m_b):
        raise TypeError("m_b must be a list of lists")
    elif m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    elif not all(
            isinstance(n, int) or isinstance(n, float) for n in [
                ele for r in m_a for ele in r]):
        raise ValueError("m_a should contain only integers or floats")
    elif not all(
            isinstance(n, int) or isinstance(n, float) for n in [
                ele for r in m_b for ele in r]):
        raise ValueError("m_b should contain only integers or floats")
    for r_a in m_a:
        if len(r_a) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for r_b in m_b:
        if len(r_b) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    mul = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            n = 0
            for k in range(len(m_b)):
                n += m_a[i][k] * m_b[k][j]
            row.append(n)
        mul.append(row)
    return mul
