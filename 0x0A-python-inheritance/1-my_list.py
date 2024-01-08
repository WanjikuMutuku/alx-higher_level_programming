#!/usr/bin/python3
"""
Module with class MyList
"""


class MyList(list):
    """ class with method print_sorted """
    pass

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """

        sorted_list = sorted(self)
        print(sorted_list)
