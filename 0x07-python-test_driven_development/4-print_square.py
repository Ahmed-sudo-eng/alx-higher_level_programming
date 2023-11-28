#!/usr/bin/python3
"""
This module contain a function that prints a square with the character #
"""


def print_square(size):
    """This function prints a square with the character # """
    # Checking size type and value
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    # Printing the square
    for h in range(size):
        for w in range(size):
            print('#', end='')
        print()
