#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0  # public class attribute
    print_symbol = '#'  # public class attribute

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Return the printable representation of Rectangle."""
        if self.__height == 0 or self.__width == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width]
                         * self.__height)

    def __repr__(self):
        """Return the string representation of Rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete Rectangle object."""
        Rectangle.number_of_instances -= 1  # decrement the number of instances
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on the area.
        Args:
            rect_1 (Rectangle): The first rectangle
            rect_2 (Rectangle): The second rectangle
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle
        Returns:
            Rectangle: The rectangle with bigger area, or rect_1 if both
                       have the same area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2

        return rect_1

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size.
        Args:
            size (int): The width and height of the new Rectangle.
        """
        return cls(size, size)
