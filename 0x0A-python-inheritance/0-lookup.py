#!/usr/bin/python3
"""Defines a function for object attribute lookup."""

def lookup(obj):
    """Returns a list of available attributes for the given object."""
    return dir(obj)
