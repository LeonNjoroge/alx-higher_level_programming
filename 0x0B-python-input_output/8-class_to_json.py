#!/usr/bin/python3
"""Defines a Python script for converting a class instance to a JSON-compatible dictionary."""
    

def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure.

    Args:
        obj: An instance of a class with a simple data structure.

    Returns:
        dict: The dictionary representation of the input class instance.
    """
    return obj.__dict__