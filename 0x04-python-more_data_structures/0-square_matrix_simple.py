#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [list(map(lamda x: x ** 2, row)) for now in matrix]
