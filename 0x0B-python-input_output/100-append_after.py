#!/usr/bin/python3
"""Defines function for inserting text after specific lines in a text file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    txt = ""
    with open(filename) as read_file:
        for line in read_file:
            txt += line
            if search_string in line:
                txt += new_string

    with open(filename, "w") as write_file:
        write_file.write(txt)
