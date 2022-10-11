#!/usr/bin/python3
""" Defines a class Square """


class Square:
    """ Represents a square """
    def __init__(self, value=0):
        """ Initializes the value of the size for an instance

         Args:
           value (int): Integer to be initialized to size

         Raises:
            ValueError: if value < 0
            TypeError: if value passed is not of type (int)
        """

        try:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        except Exception:
            raise TypeError("size must be an integer")
