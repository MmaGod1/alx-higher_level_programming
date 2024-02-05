#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    # Check if m_a and m_b are non-empty lists of lists
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Check if m_a and m_b contain only integers or floats
    for row in m_a:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_b should contain only integers or floats")

    # Check if all rows of m_a and m_b have the same size
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Transpose matrix m_b
    transposed_b = [[m_b[j][i] for j in range(len(m_b))] for i in range(len(m_b[0]))]

    # Perform matrix multiplication
    result = []
    for row_a in m_a:
        new_row = []
        for row_b in transposed_b:
            dot_product = sum(a * b for a, b in zip(row_a, row_b))
            new_row.append(dot_product)
        result.append(new_row)

    return result
