#!/usr/bin/python3
# 2-square.py
"""Define a Square class."""

class Square:
    """Represent a square with a specified size.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initialize a new Square with a specified size.
    """
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
