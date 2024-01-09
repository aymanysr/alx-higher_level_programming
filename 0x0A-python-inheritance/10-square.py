#!/usr/bin/python3
"""module contains a class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation with size (constructor))"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)


    def area(self):
        """Returns area of a square"""
        return self.__size ** 2
