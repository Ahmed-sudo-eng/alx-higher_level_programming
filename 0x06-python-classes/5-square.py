#!/usr/bin/python3
""" This module a class named Square """


class Square:
    """ Square class has a size """

    def __init__(self, size=0):
        """ Initialize the instance """
        self.__size = size

    @property
    def size(self):
        """ Retrieve the size """
        return self.__size

    @size.setter
    def size(self, size):
        """ set the size """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ Calculate the area """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
