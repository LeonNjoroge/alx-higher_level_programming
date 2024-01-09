#!/usr/bin/python3
"""Definesscript for converting a JSON string to a Python object."""
import json


def from_json_string(my_str):
    """Converts a JSON string to its Python object representation.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        obj: The Python object representation of the input JSON string.
    """
    return json.loads(my_str)