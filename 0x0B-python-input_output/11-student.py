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

    def to_json(self, attrs=None):
        """ Retrieves the dictionary representation of a Student instance """
        if attrs:
            my_dict = {}
            for item in attrs:
                for key in self.__dict__.keys():
                    if key == item:
                        my_dict[key] = self.__dict__[key]
            return my_dict
        else:
            if attrs is None:
                return self.__dict__
            else:
                return {}

    def reload_from_json(self, json):
        """ Replace all the attributes of the Student instance """
        if len(json) == 0:
            return
        self.__dict__ = json
