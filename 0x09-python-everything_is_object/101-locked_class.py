#!/usr/bin/python3
class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if name == 'first_name':
            object.__setattr__(self, name, value)
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
