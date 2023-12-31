#!/usr/bin/python3
"""Define a Square class to represent a geometric square.

Attributes:
    size (int): The size of the square.
    position (tuple): The position of the square represented as a tuple (x, y).

Methods:
    __init__(self, size=0, position=(0, 0)): Initialize a new Square size
    size(self): Get/set the current size of the square using a property.
    position(self): Set the current position of the square.
    area(self): Return the current area of the square.
    my_print(self): Print the square with the '#' character.
    __str__(self): Define the string representation of a Square.
"""


class Square:
    """Represent a square with a specified size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square.
        Raises:
            TypeError: If size is not an integer or if position
            is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position of the square.
        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the '#' character, position."""
        if self.__size == 0:
            print("")
            return

        [print("") for m in range(0, self.__position[1])]
        for m in range(0, self.__size):
            [print(" ", end="") for n in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the string representation of a Square."""
        if self.__size != 0:
            [print("") for m in range(0, self.__position[1])]
        for m in range(0, self.__size):
            [print(" ", end="") for n in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if m != self.__size - 1:
                print("")
        return ""
