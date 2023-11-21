#!/usr/bin/python3
""" This module defines a class Square that defines asquare by size """


class Square:
    """ This class defines a square defined by size
    and have a method to calculate Area """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ Public instance method that returns the current square area """
        return self.__size ** 2
