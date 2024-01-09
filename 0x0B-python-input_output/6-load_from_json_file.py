#!/usr/bin/python3
""" module with method load_from_json_file """

import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file” """
    with open(filename, 'r', encoding="UTF-8") as file:
        return json.load(file)
