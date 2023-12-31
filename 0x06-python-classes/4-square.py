#!/usr/bin/python3
""" This module contains a Square class that defines a square by it's size """


class Square:
    """ This class defines a square by it's size """

    def __init__(self, size=0):
        """ Initialize the object """
        self.__size = size

    @property
    def size(self):
        """ Retrive the size (getter) """
        return self.__size

    @size.setter
    def size(self, size):
        """ set the size (setter) """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ Calculate the area """
        return self.__size ** 2
