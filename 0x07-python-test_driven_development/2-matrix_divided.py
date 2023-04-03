#!/usr/bin/python3
"""divede numbers within 2d matrix"""
def matrix_divided(matrix, div):
    """ Goes through matrix and divide each number by divisor"""
    for i in range(len(matrix)):
        for j in matrix[i]:
            if type(j) not in [float, int]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if (i < len(matrix)-1):
            if len(matrix[i]) is not len(matrix[i+1]):
                raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div,(int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(j / div, 2) for j in x] for x in matrix]
