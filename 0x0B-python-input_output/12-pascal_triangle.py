#!/usr/bin/python3

"""Defines a function to generate Pascal's Triangle."""


def pascal_triangle(n):
    """Generate Pascal's Triangle up to the given number of rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: A list of lists of integers representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        row = [1]
        for i in range(len(triangle[-1]) - 1):
            row.append(triangle[-1][i] + triangle[-1][i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
