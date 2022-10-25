#!/usr/bin/python3
""" dwfines a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square instance"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        super().__init__(self.__size, self.__size)
        return super().__str__()
