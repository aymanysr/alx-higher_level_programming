#!/usr/bin/python3

if __name__ == "__main__":
    """Print add, sub, mul and div of a & b"""
    from calculator_1 import add, sub, mul, div

    a = 5
    b = 10

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
