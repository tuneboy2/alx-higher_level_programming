#!/usr/bin/python3
""" Defines a class Square """


class Square:
    """ Represents a square """
    def __init__(self, value=0):
        """ Initializes parameters to self

        Args:
            value: the size of the square
            """
        self.size = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            assert type(value) == int
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        except AssertionError:
            raise TypeError("size must be an integer")

    def area(self):
        """ Returns the area of a square """
        return self.size ** 2
