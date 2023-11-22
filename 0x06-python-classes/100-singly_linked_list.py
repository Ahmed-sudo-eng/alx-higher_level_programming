#!/usr/bin/python3
""" This module defines tow classes: a Node and a SinglyLinkedList """


class Node:
    """ This class has data and next_node as attributes """

    def __init__(self, data, next_node=None):
        """ Initalize the attributes """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ Retrieve the data """
        return self.__data

    @data.setter
    def data(self, value):
        """ Set the data """
        if type(data) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """ Retrieve next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ apointer to the next node """
        if (type(value) is not Node) or (type(value) is not None):
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ This class has head as attribute """

    def __init__(self):
        """Intialize the list """
        self.__head = []

    def sorted_insert(self, value):
        """ Add a node to the list """
        self.__head.append(value)
        self.__head.sort()

    def __str__(self):
        """ A string representing the class """
        for i in self.__head:
            print(i)
        return ""
