#!/usr/bin/python3
""" N queens puzzle challenge module """
import sys


def nqueens(N):
    """ find every possible non-attacking queen """

    def is_safe(row, col):
        """ check if a queen be placed at this location """

        for i in range(row):
            if board[i] == col:
                return False
            elif board[i] - i == col - row:
                return False
            elif board[i] + i == col + row:
                return False
        return True

    def solve_nqueens(row):
        """ find a valid locations """

        if row == N:
            solutions.append(list(board))
            return

        for col in range(N):
            if is_safe(row, col):
                board[row] = col
                solve_nqueens(row + 1)                
                board[row] = col

    board = [-1] * N
    solutions = []
    solve_nqueens(0)

    for solution in solutions:
        formatted_solution = [[i, col] for i, col in enumerate(solution)]    
        print(formatted_solution)


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
