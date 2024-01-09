#!/usr/bin/python3
"""module for matrix_divided method"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        matrix (list): matrix to be divided
        div (int): divisor
    Raises:
        TypeError: if matrix is not a list of lists of integers or floats
        TypeError: if matrix contains rows of different sizes
        TypeError: if div is not an integer or float
        ZeroDivisionError: if div is zero
        Returns:
            The matrix divided by div
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
