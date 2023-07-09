#!/usr/bin/python3
"""matrix multiplaication function"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """The multiplication of two matrices

    Args:
        m_a (list of lists of ints or floats): the matrix a
        m_b (list of lists of ints or floats): the matrix b
    """

    return (np.matmul(m_a, m_b))
