#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """write a str to a txt file (UTF8) and return the number of chars written.
    Args:
        filename (str): The name of the file to write.
        text (str): The string to write to the file.
    Returns:
        The number of characters written.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
