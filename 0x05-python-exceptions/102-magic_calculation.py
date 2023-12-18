#!/usr/bin/python3

def magic_calculation(a, b):

    val = 0

    for m in range(1, 3):
        try:
            if m > a:
                raise Exception('Too far')

            else:
                val += a ** b / m

        except Exception:
            val = b + a
            break

    return val
