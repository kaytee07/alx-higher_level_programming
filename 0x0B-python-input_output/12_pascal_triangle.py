#!/usr/bin/python3
"""This module defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's Triangle of size n.
    Each element of the returned list is a list containing the elements of a
    row in Pascal's Triangle.

    Args:
        n: An integer representing the size of the desired Pascal's Triangle.
            Must be greater than or equal to 1.

    Returns:
        A list of lists representing Pascal's Triangle of size n.

    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
