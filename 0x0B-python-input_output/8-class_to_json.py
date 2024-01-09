#!/usr/bin/python3
"""Defines script for converting a class instance to a JSON dictionary."""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure.

    Args:
        obj: An instance of a class with a simple data structure.

    Returns:
        dict: The dictionary representation of the input class instance.
    """
    return obj.__dict__
