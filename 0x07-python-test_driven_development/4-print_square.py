#!/usr/bin/python3
"""
Module: print_square
Description: Prints a square with the character #.
"""

def print_square(size):
    """
    Prints a square where size is
    the length and width of the square.
    """

    # Check if size is an integer
    if type(size) is not int:
        raise TypeError("size must be an integer")

    # Check if size is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Loop to print the square with the character #
    for m in range(size):
        for n in range(size):
            print('#', end='')
        print()
