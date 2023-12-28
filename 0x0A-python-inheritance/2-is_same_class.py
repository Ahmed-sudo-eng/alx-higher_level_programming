#!/usr/bin/python3
"""
This Module contain a function "is_same_class" that returns True if the object
is exactly an instance of the specified class; otherwise False
"""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an instance of the specified
        class, otherwise return False
    """
    if (type(obj) is a_class) and isinstance(obj, a_class):
        return True
    else:
        return False
