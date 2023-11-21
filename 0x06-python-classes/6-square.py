#!/usr/bin/python3
""" This module contains a Square class that defines a square by it's size """


class Square:
    """ This class defines a square by it's size """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize the size """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.size = size
            self.__size = size
        self.__position = position

    def size(self):
        """ a getter to retrieve the size """
        return self.size

    def size(self, value):
        """ a setter to set the size """
        self.size = value

    def position(self):
        """ a getter to retrive the position """
        return self.__position

    def position(self, value):
        """a setter to set the position """
        if (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position[0] = value[0]
            self.__position[1] = value[1]

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

