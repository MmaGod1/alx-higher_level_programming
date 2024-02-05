#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        list of lists: Result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists, or not a rectangle.
        ValueError: If m_a or m_b is empty or if matrices can't be multiplied.
    """
    # Validation
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")
    
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a and m_b must be lists of lists")
    
    if any(not row for row in m_a) or any(not row for row in m_b):
        raise ValueError("m_a and m_b can't contain empty rows")
    
    if any(not all(isinstance(ele, (int, float)) for ele in row) for row in m_a) or \
       any(not all(isinstance(ele, (int, float)) for ele in row) for row in m_b):
        raise TypeError("m_a and m_b should contain only integers or floats")

    if len(set(len(row) for row in m_a)) != 1 or len(set(len(row) for row in m_b)) != 1:
        raise ValueError("all rows of m_a and m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a columns must match m_b rows for multiplication")

    # Matrix multiplication
    result = [[0] * len(m_b[0]) for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
