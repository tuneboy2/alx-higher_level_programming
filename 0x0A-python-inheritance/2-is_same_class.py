#!/usr/bin/python3
""" Module defines an is_same_class function"""


def is_same_class(obj, a_class):
    """ A function that checks if the object is exactly an instance
    of the specified class"""
    return isinstance(obj, a_class)
