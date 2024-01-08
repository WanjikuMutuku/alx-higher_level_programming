#!/usr/bin/python3
""" Module with method is_same_class """


def is_same_class(obj, a_class):
    """ Mthod that returns True if the object is exactly, False otherwise """
    return type(obj) is a_class
