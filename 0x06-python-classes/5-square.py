#!/usr/bin/python3
""" This module contains a Square class that defines a square by it's size """


class Square:
    """ This class defines a square by it's size """

    def __init__(self, size=0):
        """ Initialize the size """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.size = size
            self.__size = size

    def size(self):
        """ a getter to retrieve the size """
        return self.size

    def size(self, value):
        """ a setter to set the size """
        self.size = value

    def area(self):
        """ Calculate the area and returns it """
        return self.size ** 2

    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for i in range(self.size):
                    print('#', end="")
                print()
