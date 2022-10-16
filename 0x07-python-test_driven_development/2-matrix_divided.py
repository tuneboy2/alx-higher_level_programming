#!/usr/bin/python3
""" Defines a function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ Returns a list of lists containing a mayrix divided by an element

    Args:
        matrix: a list of lists of integers or floats
        div (int): the element

    Raises:
        TypeError:
            - if the matrix elements are not of type int or float
            - if the matrix rows is not of same size
            - if the div parameter is not of type int or float

        ZeroDivisionError:
            - if the div parameter is equal to zero (0)
    """

    new_matrix = []
    i = 0

    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of "
        "integers/floats")

    for row in matrix:
        if i == 0:
            row_length = len(row)
            i += 1
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        new = []
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("matrix must be a matrix"
                " (list of lists) of integers/floats")

            if type(div) not in [int, float]:
                raise TypeError("div must be a number")

            new.append(round(elem / div, 2))
        new_matrix.append(new)

    return new_matrix
