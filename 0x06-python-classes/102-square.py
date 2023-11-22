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

    def __eq__(self, other):
        """ check equallity for areas """
        return self.area() == other.area()

    def __gt__(self, other):
        """ check if self area greater than or equal other area """
        return self.area() > other.area()

    def __ge__(self, other):
        """ check if self area greater than other area """
        return self.area() >= other.area()

    def __lt__(self, other):
        """ check if self area less than other area """
        return self.area() < other.area()

    def __le__(self, other):
        """ check if self area less than or equal other area """
        return self.area() <= other.area()
