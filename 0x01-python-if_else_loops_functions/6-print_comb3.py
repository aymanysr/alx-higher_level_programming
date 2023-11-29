#!/usr/bin/python3

dig1 = 0

while dig1 < 9:
    dig2 = dig1 + 1

    while dig2 < 10:
        if dig1 < 8:
            print("{:d}{:d}, ".format(dig1, dig2), end='')
        else:
            print("{:d}{:d}".format(dig1, dig2))

        dig2 += 1

    dig1 += 1
