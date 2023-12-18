#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    val = []
    total = 0

    for m in range(0, list_length):
        try:
            total = my_list_1[m] / my_list_2[m]

        except TypeError:
            total = 0
            print("wrong type")

        except ZeroDivisionError:
            total = 0
            print("division by 0")

        except IndexError:
            total = 0
            print("out of range")

        finally:
            pass

        val.append(total)

    return val
