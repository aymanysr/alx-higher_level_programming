#!/usr/bin/python3
def uniq_add(my_list=[]):

    unique_numbers = set()

    for elem in my_list:
        unique_numbers.add(elem)

    sum_of_unique = sum(unique_numbers)

    return sum_of_unique
