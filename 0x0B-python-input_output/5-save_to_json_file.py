#!/usr/bin/python3
"""module for save_to_json_file method"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
        my_obj (obj): object to be written to file
        filename (str): name of file to write to

    Returns:
        None
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
