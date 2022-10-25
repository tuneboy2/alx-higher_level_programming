#!/usr/bin/python3
""" Define a class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
