#!/usr/bin/python3
"""module for the class 'square'"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """"square representation"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor for the class 'square'"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for the size attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns a string representation of the class 'square'"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)


if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
