#!/usr/bin/python3
""" N queens puzzle challenge module """
import sys


def nqueens(x):
    """ find every possible non-attackin queen """

    def solution(ans, row, col):
        """ check if a queen can be placed at this location """

        for i in range(row):
            if pos[i][col] == 'Q':
                return False
            elif col - i >= 0 and pos[row - i][col - i] == 'Q':
                return False
            elif col + i < x and pos[row - i][col + i] == 'Q':
                return False
        return True

    def backtrack(row):
        """ find a valid solution """

        if row == x:
            ansr = []
            for i in range(x):
                for j in range(x):
                    if pos[i][j] == 'Q':
                        ansr.append([i, j])
            ans.append(ansr)
            return
        for col in range(x):
            if solution(ans, row, col):
                pos[row][col] = 'Q'
                backtrack(row + 1)
                pos[row][col] = '.'

    pos = [['.' for _ in range(x)] for _ in range(x)]
    ans = []
    backtrack(0)
    for r in ans:
        print(r)


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
