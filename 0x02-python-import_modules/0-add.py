#!/usr/bin/python3

a = 1
b = 2
exec_string = 'from add_0 import add\nsum = add({}, {})'.format(a, b)
exec(exec_string)

print("{} + {} = {}".format(a, b, sum))
