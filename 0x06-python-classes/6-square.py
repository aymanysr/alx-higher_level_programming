#!/usr/bin/python3
"""Square module."""


class Square:
    """This is a class representing a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.
        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        Raises:
            TypeError: If size != int or position != tuple of 2 positve ints
            ValueError: If size < 0 or position contains negatve ints
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Get the position of the square.
        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.
        Args:
            value (tuple): The new position of the square.
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If value contains negative integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints a square using the '#' character.
        If the size of the square is 0, it prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for _ in range(0, self.__size):
            [print(" ", end="") for x in range(0, self.__position[0])]
            [print("#", end="") for y in range(0, self.__size)]
            print("")
