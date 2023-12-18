#!/usr/bin/python3

def uniq_add(my_list=[]):
    other = set(my_list)
    count = 0

    for m in other:
        count = count + m
    return count
