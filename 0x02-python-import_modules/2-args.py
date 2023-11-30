#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argument = sys.argv

    length = len(argument) - 1

    if length > 1:
        print(length, 'arguments:')

        for m in range(1, length + 1):
            print('{:d}: {}'.format(m, argument[m]))
    elif length == 1:
        print(length, 'argument:')
        
        for m in range(m, length + 1):
            print('{:d}: {}'.format(m, argument[m]))
    elif length == 0:
        print(length, 'arguments.')