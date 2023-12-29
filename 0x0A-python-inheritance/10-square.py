#!/usr/bin/python3
"""
This module contain Square class which inherits from Rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ This class inherits from Rectangle """

    def __init__(self, size):
        """ Initializes the properties """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Calculate the area """
        return self.__size ** 2

    def __str__(self):
        """ return a string that represent the square """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
