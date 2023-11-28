#!/usr/bin/python3
def upp(val):
    if ord(val) >= 97 and ord(val) <= 122:
        return (ord(val) - 32)
    else:
        return ord(val)


def uppercase(str):
    line = ""
    for val in str:
        line += "%c" % upp(val)
    print("{:s}".format(line))
