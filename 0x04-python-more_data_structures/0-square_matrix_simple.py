#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for col in matrix:
        new_row = [x**2 for x in col]
        new_matrix.append(new_row)
    return new_matrix
