#!/usr/bin/python
"""module for inherits_from method"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False

    Arguments:
        obj {[type]} -- [description]
        a_class {[type]} -- [description]
    Returns:
        [type] -- [description]

    """
    return isinstance(obj, a_class) and type(obj) != a_class
