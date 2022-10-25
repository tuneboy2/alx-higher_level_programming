#!/usr/bin/python3
""" Define a class BaseGeometry"""


class BaseGeometry:
    """An empty instance of class BaseGeometry"""
    def area(self):
        """ An undefinrd area method of class BaseGeometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ A method that validates a value

        Args:
            name (str): assume name is a string
            value (int): parameter to be validated

        Reaises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than zero")
