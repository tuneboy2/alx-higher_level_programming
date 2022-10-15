#!/usr/bin/python3
""" Defines a function that divides all elements of a matrix """

def matrix_divided(matrix, div):
    """ Returns a list of lists(matrix) containing a mayrix divided by an element

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
    ret = [[round(a / div, 2) for a in row] for row in matrix]
    return ret
