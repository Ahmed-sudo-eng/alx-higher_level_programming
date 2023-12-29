#!/usr/bin/python3
"""
This module contain "inherits_from" function that return True if the object is
an instance of the class (directly or indirectly) from the specified class;
otherwis False
"""


def inherits_from(obj, a_class):
    """ This function returns True if obj is inherited from a_class """
    return isinstance(obj, a_class) and type(obj) is not a_class
