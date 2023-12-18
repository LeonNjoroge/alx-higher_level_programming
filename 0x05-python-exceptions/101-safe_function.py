#!/usr/bin/python3

def safe_function(fct, *args):
    import sys

    try:
        val = fct(*args)
        return val

    except Exception as x:
        print("Exception: {}".format(x), file=sys.stderr)
        return None
