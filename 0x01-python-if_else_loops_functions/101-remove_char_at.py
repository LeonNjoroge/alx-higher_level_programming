#!/usr/bin/python3
def remove_char_at(str, n):
    other_str = ""
    m = 0

    for ch in str:
        if m != n:
            other_str = other_str + ch
        m = m + 1
    return other_str
