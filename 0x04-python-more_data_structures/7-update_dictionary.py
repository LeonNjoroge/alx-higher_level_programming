#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value

    else:
        for m in a_dictionary:
            if m == key:
                a_dictionary[m] = value

    return a_dictionary
