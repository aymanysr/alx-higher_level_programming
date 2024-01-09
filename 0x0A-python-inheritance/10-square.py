#!/usr/bin/python3
"""module contains a class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class inherits from Rectangle
    Instantiation with size: def __init__(self, size)
    size must be private. No getter or setter
    size must be a positive integer, validated by integer_validator
    """
    def __init__(self, size):
        """Instantiation with size (constructor))"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns area of a square"""
        return self.__size ** 2
