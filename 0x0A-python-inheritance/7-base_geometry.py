#!/usr/bin/python3
"""
This module has a class "BaseGeometry"
"""


class BaseGeometry(object):
    """ BaseGeometry class """
    def area(self):
        """ Raise an Exception with the message "area() is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This function validates value """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
