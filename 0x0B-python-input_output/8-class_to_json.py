#!/usr/bin/python3
""" module with method class_to_json """


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
    for JSON serialization of an object """
    attributes = obj.__dict__.copy()

    # Handle attributes with name mangling (for private attributes)
    for key, value in attributes.items():
        if key.startswith('_'):
            new_key = '{}{}'.format(obj.__class__.__name__, key)
            attributes[new_key] = attributes.pop(key)

    return attributes
