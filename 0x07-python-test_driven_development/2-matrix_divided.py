#!/usr/bin/python3
"""
Module: matrix_divided
Description: Divides each element of a matrix of numbers by a number
"""

def matrix_divided(matrix, div):
    """
    Returns a new matrix (list of lists)
    with the result of the division of matrix by div
    rounded to 2 decimal places.
    """

    # Check if the input matrix is a valid matrix (list of lists) of integers/floats
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    # Check each element in the matrix to ensure they are integers or floats
    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    # Check that each row of the matrix has the same size
    row_len = []
    for row in matrix:
        row_len.append(len(row))
    if not all(size == row_len[0] for size in row_len):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if the divisor is a number
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    # Check if the divisor is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division, rounding to 2 decimal places
    other_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return other_matrix
