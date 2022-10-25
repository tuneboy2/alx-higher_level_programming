#!/usr/bin/python3
""" Define a class BaseGeometry"""


class BaseGeometry:
    """An instance of class BaseGeometry"""
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
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ An instance of class Rectangle and a superclass BaseGeometry"""
    def __init__(self, width, height):
        """ Initializes the parameters passed to a variable

        Args:
            width (int): The width of the Rectangle
            height (int); The height of the Rectangle
        """
        if super().integer_validator("width", width):
            self.__width = width
        if super().integer_validator("height", height):
            self.__height = height
