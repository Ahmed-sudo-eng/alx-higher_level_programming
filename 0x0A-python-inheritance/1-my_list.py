#!/usr/bin/python3
"""
This module contains a class "MyList" that inherits from list
"""


class MyList(list):
    """ This class inherits from list class """

    def print_sorted(self):
        """ prints the sorted list """
        new_list = self.copy()
        new_list.sort()
        print(new_list)
