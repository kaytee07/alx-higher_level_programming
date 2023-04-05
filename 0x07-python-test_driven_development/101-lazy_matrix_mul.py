#!/usr/bin/python3
"""using numPy to multiply matrices"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy"""
    return np.matmul(m_a, m_b)
