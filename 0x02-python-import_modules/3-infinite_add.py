#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    val = 0

    for arg in sys.argv:
        if arg != sys.argv[0]:
            val = val + int(arg)
    print(val)
