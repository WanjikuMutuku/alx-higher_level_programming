#!/usr/bin/python3
""" Module with method Square from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Method that inherits from Rectangle """

    def __init__(self, size):
        """ Initializes a Square instance """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Returns a string representation of the Square """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
