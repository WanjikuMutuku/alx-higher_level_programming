#!/usr/bin/python3
""" Module for MyInt """


class MyInt(int):
    """MyInt inherits from int """

    def __eq__(self, other):
        """ Inverts the == operator """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Inverts the != operator """
        return super().__eq__(other)
