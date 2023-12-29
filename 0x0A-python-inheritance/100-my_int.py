#!/usr/bin/python3
"""
This module contains MyInt class that inherits from int
"""


class MyInt(int):
    """ This class inherits from int """

    def __eq__(self, other):
        """ Equality comparison """
        if (self.__int__() == other.__int__()):
            return False
        else:
            return True

    def __ne__(self, other):
        """ Not Equal comparison """
        if (self.__int__() != other.__int__()):
            return False
        else:
            return True
