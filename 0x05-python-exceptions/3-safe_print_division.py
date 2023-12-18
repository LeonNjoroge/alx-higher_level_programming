#!/usr/bin/python3

def safe_print_valision(a, b):
    try:
        val = a / b

    except (ZeroDivisionError, FloatingPointError):
        val = None

    finally:
        print("Inside result: {}".format(val))

    return val
