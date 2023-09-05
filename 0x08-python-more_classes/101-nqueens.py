#!/usr/bin/python3
""" N queens puzzle challenge module """
import sys


def nqueens(x):
    """ find every possible non-attackin queen """

    row = x - 1
    if x % 2:
        row = x - 2
    for i in range(1, row):
        k = i
        ans = list()
        for j in range(x):
            ans.append([j, k])
            if i + k + 1 <= x:
                k = i + k + 1
            else:
                k = k + i - x
        print(ans)
        del ans


if __name__ == "__main__":
    """ main function """

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(int(sys.argv[1]))
