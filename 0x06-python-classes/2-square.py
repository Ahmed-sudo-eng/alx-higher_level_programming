#!/usr/bin/python3
""" This Module defines a class Square by private instance attribute size """


class Square:
    """Square class defines a square by size """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
