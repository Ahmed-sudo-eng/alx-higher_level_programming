#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x: x, [[x ** 2 for x in row] for row in matrix]))
