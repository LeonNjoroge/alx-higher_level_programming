#!/usr/bin/python3
"""Defines a Python script for writing a Python object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes a Python object to a text file using JSON representation.

    Args:
        my_obj: The Python object to be written to the file.
        filename (str): The name of the file to save the JSON representation.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
