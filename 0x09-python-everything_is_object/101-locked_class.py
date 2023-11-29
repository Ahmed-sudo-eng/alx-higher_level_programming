#!/usr/bin/python3
"""
This module has a LockedClass with no class or object attribute. that prevents the user from dynamically creating new instance attributes, except if the new instance attribut is called first_name
"""


class LockedClass:
    """This class prevents dynamically creating attributes"""

    __slots__ = ['first_name']
