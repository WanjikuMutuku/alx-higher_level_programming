#!/usr/bin/python3
""" module with method save_to_json_file """

import json


def save_to_json_file(my_obj, filename):
    """ method that  writes an Object to a text file,
    using a JSON representation """
    with open("filename", "w") as file:
        json.dump(my_obj, file)
