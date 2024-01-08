#!/usr/bin/python3
"""Inherits from the list class"""


class MyList(list):
    """Class inheriting from list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
