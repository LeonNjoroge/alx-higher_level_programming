#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:
        return (None)

    large = my_list[0]

    for m in range(len(my_list)):
        if my_list[m] > large:
            large = my_list[m]

    return (large)
