#!/usr/bin/python3
""" 1-rectangle.py """


class Rectangle:
    """ private instance width and height are created """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    """ retrives the width """
    def width(self):
        return self.__width

    @width.setter
    """defines the exception conditions for the value of the width """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    """ retrives the height """
    def height(self):
        return self.__height

    @height.setter
    """ determines the exceptions for the height value """
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
