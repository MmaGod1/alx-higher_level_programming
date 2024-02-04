#!/usr/bin/python3
"""Defines a function to multiply two matrices."""

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
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(isinstance(ele, (int, float)) for row in m_a for ele in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(ele, (int, float)) for row in m_b for ele in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication logic
    inverted_b = [[m_b[j][i] for j in range(len(m_b))] for i in range(len(m_b[0]))]

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = sum(row[i] * col[i] for i in range(len(inverted_b[0])))
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
