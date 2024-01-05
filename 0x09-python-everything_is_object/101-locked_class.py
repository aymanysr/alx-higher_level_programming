#!/usr/bin/python3

class LockedClass:
    """A class with no class or object attribute except for first_name"""
    __slots__ = ['first_name']
    def __init__(self, first_name=""):
        self.first_name = first_name

