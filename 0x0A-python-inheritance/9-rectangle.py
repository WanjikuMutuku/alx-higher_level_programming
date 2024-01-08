#!/usr/bin/python3
""" Module for Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines the Rectangle class that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Initializes a Rectangle instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Rutuens area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns a string representation of the Rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
