#!/usr/bin/python3
"""Module for load_from_json_file method"""


import json


def load_from_json_file(filename):
    """creates an Object from a JSON file
    Args:
        filename (str): name of file to write to

    Returns:
        None
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
