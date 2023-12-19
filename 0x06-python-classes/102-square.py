#!/usr/bin/python3
"""My square module"""

class Square:
    """Define a Square class."""

    def __init__(self, size=0):
        """Create a Square.

        Args:
            size (int): Length of a side of the Square.
        """
        self.__size = size

    @property
    def size(self):
        """Get/set the length of a side of the Square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the length of a side of the Square.

        Args:
            value (int): The new size.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate the area of the Square.

        Returns:
            int: The size squared.
        """
        return self.__size * self.__size

    def __le__(self, other):
        """Check if the area of self is less than or equal to the area of other."""
        return self.area() <= other.area()

    def __lt__(self, other):
        """Check if the area of self is less than the area of other."""
        return self.area() < other.area()

    def __ge__(self, other):
        """Check if the area of self is greater than or equal to the area of other."""
        return self.area() >= other.area()

    def __ne__(self, other):
        """Check if the area of self is not equal to the area of other."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if the area of self is greater than the area of other."""
        return self.area() > other.area()

    def __eq__(self, other):
        """Check if the area of self is equal to the area of other."""
        return self.area() == other.area()