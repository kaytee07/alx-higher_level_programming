#!/usr/bin/python3
"""multiplies matrices"""

def matrix_mul(m_a, m_b):
    """this function checks input and then multiply matrices"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for x in m_a:
        if not isinstance(x, list):
            raise TypeError("m_a must be a list of lists")
        if len(x) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for a in x:
            if not isinstance(a, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for y in m_b:
        if not isinstance(y, list):
            raise TypeError("m_b must be a list of lists")
        if len(y) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for b in y:
            if not isinstance(b, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    for m in m_b:
        if len(m_a) != len(m):
            raise ValueError("m_a and m_b can't be multiplied")
        
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += m_a[i][k] * m_b[k][j]
            row.append(sum)
        result.append(row)
    return result
