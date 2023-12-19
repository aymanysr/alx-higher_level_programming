#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Safely prints the first x integers from a list.

    Args:
        my_list (list): The list of integers.
        x (int): The number of integers to print.

    Returns:
        int: The number of integers successfully printed.
    """
    elem = 0
    c = 0
    while elem is not x:
        try:
            print("{:d}".format(my_list[elem]), end="")
            c += 1
        except (ValueError, TypeError):
            pass
        elem += 1
    print()
    return c
