#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for m in sorted(a_dictionary):
        print("{:s}: {}".format(m, a_dictionary[m]))
