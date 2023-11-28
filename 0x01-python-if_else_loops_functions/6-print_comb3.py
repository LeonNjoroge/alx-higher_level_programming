#!/usr/bin/python3
val = 0
while val <= 89:
    if val % 10 == 0:
        val += 1 + val // 10
    print("{:02d}".format(val), end='\n' if val == 89 else ", ")
    val += 1
