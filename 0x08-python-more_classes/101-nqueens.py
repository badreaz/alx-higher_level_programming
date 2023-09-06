#!/usr/bin/python3
""" N queens puzzle challenge module """
import sys


def nqueens(x):
    """ find every possible non-attackin queen """

    def solution(ans, row, col):
        """ check if a queen can be placed at this location """

        for i in range(row):
            if ans[i][col] == 'Q':
                return False
            elif col - i >= 0 and ans[row - i][col - i] == 'Q':
                return False
            elif col + i < x and ans[row - i][col + i] == 'Q':
                return False
        return True

    def backtrack(row):
        """ find a valid solution """

        if row == x:
            pos.append(["".join(row) for row in ans])
            return
        for col in range(x):
            if solution(ans, row, col):
                ans[row][col] = 'Q'
                backtrack(row + 1)
                ans[row][col] = '.'
    pos = []
    ans = [['.' for _ in range(x)] for _ in range(x)]
    backtrack(0)
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
