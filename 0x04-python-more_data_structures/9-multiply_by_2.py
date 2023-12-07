#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}

    for key, value in a_dictionary.items():
        result = value * 2
        new_dictionary[key] = result

    return new_dictionary
