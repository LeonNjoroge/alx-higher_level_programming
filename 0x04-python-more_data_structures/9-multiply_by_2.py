#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_other = {}

    for m in a_dictionary:
        dict_other[m] = a_dictionary[m] * 2

    return dict_other
