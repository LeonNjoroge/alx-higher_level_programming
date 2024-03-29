#!/usr/bin/python3
"""Defines a Python script for writing text to a UTF-8 file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
