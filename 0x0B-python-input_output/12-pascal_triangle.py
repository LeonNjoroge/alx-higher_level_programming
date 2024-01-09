#!/usr/bin/python3
"""Defines a Python function for generating Pascal's Triangle."""


def pascal_triangle(n):
    """Generate Pascal's Triangle of size n.

    Args:
        n (int): The size of the Pascal's Triangle.

    Returns:
        list of lists: A list of lists of integers rep Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]

    while len(triangles) != n:
        tri_ang = triangles[-1]
        temp = [1]

        for i in range(len(tri_ang) - 1):
            temp.append(tri_ang[i] + tri_ang[i + 1])
        temp.append(1)
        triangles.append(temp)

    return triangles
