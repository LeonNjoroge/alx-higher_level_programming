#!/usr/bin/python3
for val in range(00, 100):
    print("{:02d}".format(val), end='\n' if val == 99 else ", ")
