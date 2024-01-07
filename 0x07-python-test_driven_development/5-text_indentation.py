#!/usr/bin/python3
"""
Module: text_indentation
Description: Adds two new lines after a set of characters.
"""

def text_indentation(text):
    """
    Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.
    """

    # Check if text is a string
    if type(text) is not str:
        raise TypeError("text must be a string")

    # Iterate over each delimiter and add two newlines after it
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    # Print the formatted text
    print("{}".format(text), end="")
