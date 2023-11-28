#!/usr/bin/python3
for m in range(122, 96, -1):
    if m % 2 != 0:
        m = m - 32
    print("{}".format(chr(m)), end="")