#!/usr/bin/python3
"""Implements a function for checking object class."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The target class for comparison.

    Returns:
        True if obj is an instance of a_class, otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
