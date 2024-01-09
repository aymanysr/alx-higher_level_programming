#!/usr/bin/python3
"""Module contains a class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of a Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of a Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
