#!/usr/bin/python3
""" Module for add_attribute function """


def add_attribute(obj, name, value):
    """ Adds a new attribute to an object if it's possible """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
