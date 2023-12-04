#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            print("{:d}".format(matrix[m][n]), end="")

            if n != (len(matrix[m]) - 1):
                print(" ", end="")

        print("")
