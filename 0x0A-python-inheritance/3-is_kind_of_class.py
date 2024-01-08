#!/usr/bin/python3
""" Module with method is_kind_of_class """

def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of a class
    inherited from, False otherwise """

    return isinstance(obj, a_class)
