#!/usr/bin/python3
"""module for the class 'base'"""


class Base:
    """class 'base'"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of the class 'base'"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
