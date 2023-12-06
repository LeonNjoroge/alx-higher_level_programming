#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_other = [[m ** 2 for m in row] for row in matrix]
    return matrix_other
