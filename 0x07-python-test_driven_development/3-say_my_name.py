#!/usr/bin/python3
""" Defines a function that prints a Full name"""


def say_my_name(first_name, last_name=""):
    """ Function that prints the First name and the Last name

    Args:
    first_name (string): The First name
    last_name (string): The Last name

    Raises:
    TypeError: if parameter passed is not of type stting
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
