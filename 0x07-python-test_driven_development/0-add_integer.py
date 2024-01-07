#!/usr/bin/python3
"""
Module: add_integer
Description: Adds two integers together
"""


def add_integer(a, b=98):
    """
    Returns the addition of a and b,
    or raises an error if a and b are not integers or floats
    """

    # Check if 'a' is an integer or float
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    # Check if 'b' is an integer or float
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    # Convert 'a' and 'b' to integers if they are floats
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    # Return the addition of 'a' and 'b'
    return a + b
