#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    number_arg = len(sys.argv) - 1

    if number_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")

        sys.exit(1)

    val = sys.argv[2]

    if val != '+' and val != '-' and val != '*' and val != '/':
        print("Unknown operator. Available operators: +, -, * and /")

        sys.exit(1)

    from calculator_1 import add, sub, mul, div

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if val == '+':
        print(f"{a} + {b} = {add(a, b)}")
    elif val == '-':
        print(f"{a} - {b} = {sub(a, b)}")
    elif val == '*':
        print(f"{a} * {b} = {mul(a, b)}")
    else:
        print(f"{a} / {b} = {div(a, b)}")
