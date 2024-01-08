#!/usr/bin/python3
""" Module with method BaseGeometry """


class BaseGeometry():
    """ An empty class """
    def area(self):
        """ method that raises an exception with an area not implemented """
        raise Exception("area() is not implemented")
