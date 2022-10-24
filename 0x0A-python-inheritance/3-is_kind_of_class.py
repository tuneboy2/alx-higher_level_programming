#!/usr/bin/python3
""" Dedines a Function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """ Defines if an object is an instance of the class, or if the
    object is an instance of a class that inherited from

    Args:
        obj (class): Parameter to be checked
        a_class (class): Class parameter obj is to be checked against

    Return:
        True if an instamce of a class or an instance of a subclass of a class
        Otherwise, False.
    """
    return isinstance(obj, a_class)
