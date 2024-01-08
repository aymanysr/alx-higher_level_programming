#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes.
    Args:
        obj (any): The object to look up.
    Returns:
        list: A list of all available attributes.
    """
    return dir(obj)
