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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ defines the area of a rectangle

        Return:
            The area obtained
        """
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
