#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''Computes the square value of all integers of a matrix.

        Matrix is a 2 dimensional array
        It Returns a new matrix which is Same size as matrix
        Each value should be the square of the value of the input
        Initial matrix should not be modified
    '''
    new = [[col ** 2 for col in row] for row in matrix]
    return new
