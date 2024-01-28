#!/usr/bin/python3
"""

This module defines a matrix division function

"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix by a given number

    Args:
        matrix: a list of lists (matrix) - members can be of type ints or floats
        div: number to be used for the division (can be a float or an integer)
    Raises:
        TypeError: if the matrix contains non-numbers
        TypeError: if the matrix contains rows of diff sizes
        TypeError: if div is not an int or float
        ZeroDivisionError: if div is 0
    Returns:
        A new matrix which rep the results of the division
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
