#!/usr/bin/python3
"""module for is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """returns True if obj is instance of a_class or a class that inherited
    from a_class, otherwise False"""
    return isinstance(obj, a_class)
