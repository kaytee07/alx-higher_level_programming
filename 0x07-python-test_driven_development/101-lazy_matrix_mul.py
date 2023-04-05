import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    m_a = np.array(m_a)
    m_b = np.array(m_b)

    if m_a.size == 0 or m_a.shape[1] == 0:
        raise ValueError("m_a can't be empty")

    if m_b.size == 0 or m_b.shape[1] == 0:
        raise ValueError("m_b can't be empty")

    if m_a.shape[1] != m_b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    result = np.dot(m_a, m_b)

    return result.tolist()
