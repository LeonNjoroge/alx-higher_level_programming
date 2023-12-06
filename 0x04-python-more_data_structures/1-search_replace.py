#!/usr/bin/python3
def search_replace(my_list, search, replace):
    other = []

    for m in range(len(my_list)):
        if my_list[m] == search:
            other.append(replace)

        else:
            other.append(my_list[m])
    return other
