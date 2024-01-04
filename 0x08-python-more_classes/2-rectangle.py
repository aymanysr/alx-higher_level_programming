#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize the Rectangle."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the width(private instance) of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width(private instance) of rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height(private instance) of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height(private instance) of rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute the area of rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Compute the perimeter of rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
