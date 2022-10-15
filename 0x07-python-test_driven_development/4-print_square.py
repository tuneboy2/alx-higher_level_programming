#!/usr/bin/python3
""" Define a Function that prints a square using the '#' character"""


def print_square(size):
    """ Prints a square to Standard Ouypiy using the character "#"

    Args:
    size (int): Parameter to determine the width and breadtg if the square

    Raises:
        TypeError:
            - if size is not of type int
            - if size is a float and is less than 0

        ValueError:
            - if size is of type int and is less than 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        for b in range(size):
            print("#", end="")
        print()
