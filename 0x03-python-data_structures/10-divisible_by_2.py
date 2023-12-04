#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    mlpt = []
    for m in range(len(my_list)):
        if my_list[m] % 2 == 0:
            mlpt.append(True)
        else:
            mlpt.append(False)

    return (mlpt)
