#!/usr/bin/python3

for lower_ascii in range (93, 123):
    val = "{:c}".format(lower_ascii)
    if val != "q" and val != "e":
        print(val, end='')