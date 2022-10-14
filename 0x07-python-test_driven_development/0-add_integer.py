#!/usr/bin/python3
"""
    This Module contains a method that adds two integers


"""


def add_integer(a, b=98):
    """ Adds Two integers together
        Parameters a and b must be of type int or float, otherwise
        raise a TyoeError("a must be an integer or b must be an integer")"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
