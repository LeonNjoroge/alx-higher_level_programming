#!/usr/bin/python3
"""Define a Square class to represent a geometric square.

Attributes:
    size (int): The size of the square.

Methods:
    __init__(self, size): Initialize a new Square with a specified size.
    size(self): Get/set the current size of the square using a property.
    area(self): Return the current area of the square.
    my_print(self): Print the square with the '#' character.
"""

class Square:
    """Represent a square with a specified size."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the '#' character."""
        for m in range(0, self.__size):
            [print("#", end="") for n in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")