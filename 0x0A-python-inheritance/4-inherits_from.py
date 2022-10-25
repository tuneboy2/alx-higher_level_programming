#!/usr/bin/python3
""" Defines a function inherits_from"""


def inherits_from(obj, a_class):
    """ Defines a function that checks if an object is an instance
    of a class thats inherited from a specified class.

    Args:
        obj (class): Parameter to be checked
        a_class (class): Parameter to be checked against

    Return:
        True: if the object is an instance
        False: if otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
