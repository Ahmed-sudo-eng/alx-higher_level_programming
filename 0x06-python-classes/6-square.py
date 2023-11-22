#!/usr/bin/python3
""" This module have a Square class """


class Square:
    """ a Square class definef by size and position """

    def __init__(self, size=0, position=(0,0)):
        """ Initialize the attributes """
        if type(position) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ get the size """
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

    @property
    def position(self):
        """ get the position """
        return self.__position

    @position.setter
    def position(self, value):
        """ set the position """
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position[0] = value[0]
            self.__position[1] = value[1]

    def area(self):
        """calculate the area """
        return self.__size ** 2

    def my_print(self):
        """ Print the Square """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for s in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
