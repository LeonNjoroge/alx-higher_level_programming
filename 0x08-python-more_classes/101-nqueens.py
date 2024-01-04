#!/usr/bin/python3
"""
Solves the N-queens puzzle
"""

import sys


def initialize_board(size):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    chessboard = []
    [chessboard.append([]) for i in range(size)]
    [row.append(' ') for i in range(size) for row in chessboard]
    return chessboard


def copy_chessboard(chessboard):
    """Return a deepcopy of a chessboard."""
    if isinstance(chessboard, list):
        return list(map(copy_chessboard, chessboard))
    return chessboard


def get_solution(chessboard):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(chessboard)):
        for c in range(len(chessboard)):
            if chessboard[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def mark_attacked(chessboard, row, col):
    """Mark spots on a chessboard attacked by a queen."""
    # Mark all forward spots
    for c in range(col + 1, len(chessboard)):
        chessboard[row][c] = "x"
    # Mark all backwards spots
    for c in range(col - 1, -1, -1):
        chessboard[row][c] = "x"
    # Mark all spots below
    for r in range(row + 1, len(chessboard)):
        chessboard[r][col] = "x"
    # Mark all spots above
    for r in range(row - 1, -1, -1):
        chessboard[r][col] = "x"
    # Mark all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # Mark all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1
    # Mark all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # Mark all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


def recursive_solve(chessboard, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        chessboard (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(chessboard):
        solutions.append(get_solution(chessboard))
        return solutions

    for col in range(len(chessboard)):
        if chessboard[row][col] == " ":
            temp_chessboard = copy_chessboard(chessboard)
            temp_chessboard[row][col] = "Q"
            mark_attacked(temp_chessboard, row, col)
            solutions = recursive_solve(temp_chessboard, row + 1,
                                        queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_board(int(sys.argv[1]))
    solutions = recursive_solve(chessboard, 0, 0, [])
    for sol in solutions:
        print(sol)
