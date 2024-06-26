#!/usr/bin/python3

"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication using Numpy

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        numpy.darray: The result of multiplying the two matrices.
    """
	return np.matmul(m_a, m_b)
