#!/usr/bin/python3
"""the class 'student'"""


class Student:
    """student representation"""
    def __init__(self, first_name, last_name, age):
        """initialization of the class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of a Student Instance"""
        return self.__dict__
