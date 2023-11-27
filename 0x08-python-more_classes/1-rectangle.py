#!/usr/bin/python3
"""
This module contains an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """An empty class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the attributes"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    """Retrieve the height"""
    def height(self):
        return self.__height

    @height.setter
    """Set the height"""
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
