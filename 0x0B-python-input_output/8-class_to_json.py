#!/usr/bin/python3
""" module with method class_to_json """


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
    for JSON serialization of an object """
    return vars(obj)
