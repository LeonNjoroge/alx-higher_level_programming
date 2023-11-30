#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    a = len(sys.argv) - 1
    if a == 0:
        print(f"{a} arguments.")
    elif a == 1:
        print(f"{a} argument:")
    else:
        print(f"{a} arguments:")

    if a >= 1:
        a = 0
        for arg in sys.argv:
            if a != 0:
                print(f"{a}: {arg}")
            a = a + 1
