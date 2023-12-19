#!/usr/bin/python3
"""
Define a Square class representing a geometric square.

Attributes:
    __size (int): Size of the square.

Methods:
    __init__(self, size): Initialize a new Square with a specified size.
"""

class Square:
    """
    Represents a square.

    Attributes:
        __size (int): Size of the square.

    Methods:
        __init__(self, size): Initialize a new Square with a specified size.
    """
    def __init__(self, size):
        """Initialize a new Square with a specified size."""
        self.__size = size