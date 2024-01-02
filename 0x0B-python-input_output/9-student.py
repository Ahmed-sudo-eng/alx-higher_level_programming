#!/usr/bin/python3
"""
This module contains the class 'Student' which defines a student by: first_name
, last_name and age
"""


class Student:
    """ This class defines a studen by first name, last name and age """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves the dictionary representation of a Student instance """
        return self.__dict__
