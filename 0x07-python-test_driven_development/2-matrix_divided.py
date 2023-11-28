#!/usr/bin/python3
"""
This module contain a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix"""
    # Checking that matrix is a list
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    # Checking that matrix contains only lists
    for row in matrix:
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    # Checking that every list in the matrix contains only integers or floats
    for row in matrix:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    # Checking that the matrix have rows of equal size
    size = len(matrix[0]) # Taking the size of the first row as a reference
    for row in matrix:
        if len(row) != size:
            raise TypeError('Each row of the matrix must have the same size')
    # Checking that div is only integer or float
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    # Checking that div is not equal to ZERO
    if div == 0:
        raise ZeroDivisionError('division by zero')

    # Performing the division opreation
    new_matrix = []
    for row in matrix:
        new_matrix.append(row.copy())
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)
            j += 1
        i += 1
    return new_matrix
