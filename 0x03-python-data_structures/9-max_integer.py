#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None

    maximum = my_list[0]
    for element in my_list:
        if element > maximum:
            maximum = element

    return maximum
