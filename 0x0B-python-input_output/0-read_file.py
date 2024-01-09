#!/usr/bin/python3
"""Defines a script for reading and printing contents of a UTF-8 text file."""


def read_file(filename=""):
    """Reads and prints a UTF-8 text file to the standard output."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
