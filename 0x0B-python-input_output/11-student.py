#!/usr/bin/python3
""" module with class Student """


class Student:
    """ Student class with attributes: first, last names and age """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student """
        if attrs is None:
            return self.__dict__
        new_dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dictionary[key] = value
        return new_dictionary

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for key, value in json.items():
            setattr(self, key, value)
