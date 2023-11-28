#!/usr/bin/python3

for lower_ascii in range(ord('a'), ord('z') + 1):
    if lower_ascii != "q" or lower_ascii != "e":
        print(chr(lower_ascii), end=' ')
