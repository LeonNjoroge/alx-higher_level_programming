#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for key_val in list(a_dictionary):

        if a_dictionary[key_val] == value:

            del a_dictionary[key_val]
    return a_dictionary
