#!/usr/bin/python3
"""Defines script for reading a JSON file and creating object."""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        obj: The Python object created from the JSON file.
    """
    with open(filename) as file:
        return json.load(file)
