#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    sum = 0

    for m in range(0, x):
        try:
            print("{:d}".format(my_list[m]), end="")
            sum = sum + 1

        except (ValueError, TypeError):
            pass

    print()

    return sum
