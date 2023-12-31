#!/usr/bin/python3
"""Define a MagicClass based on a given ByteCode."""
import math


class MagicClass:
    """Represent a class with magic calculations."""

    def __init__(self, radius=0):
        """Initialize the MagicClass.

        Args:
            radius (int or float): The radius of the MagicClass.
        Raises:
            TypeError: If radius is not a number (int or float).
        """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Calculate the area of the MagicClass.

        Returns:
            float: The area of the MagicClass.
        """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the MagicClass.

        Returns:
            float: The circumference of the MagicClass.
        """
        return 2 * math.pi * self._MagicClass__radius
