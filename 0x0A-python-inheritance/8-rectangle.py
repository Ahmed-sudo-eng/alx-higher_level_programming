#!/usr/bin/python3
"""
This module conatain the class Rectangle which inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This class inherits from BaseGeometry """
    def __init__(self, weight, height):
        """ Initialize the properties """
        super().integer_validator("weight", weight)
        super().integer_validator("height", height)
        self.__weight = weight
        self.__height = height
