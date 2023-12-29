#!/usr/bin/python3
"""
This module conatain the class Rectangle which inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This class inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Initialize the properties """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculate the area """
        return self.__width * self.__height

    def __str__(self):
        """ return a formatted string that represent the rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
