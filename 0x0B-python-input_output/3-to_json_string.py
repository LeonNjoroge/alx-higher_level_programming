#!/usr/bin/python3
"""Defines a Python script for converting a Python object to a JSON string."""
import json


def to_json_string(my_obj):
    """Converts a Python object to its JSON representation.

    Args:
        my_obj: The Python object to be converted to JSON.

    Returns:
        str: The JSON representation of the input Python object.
    """
    return json.dumps(my_obj)