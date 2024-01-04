#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        list of lists: Resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists, or contains non-integer/float elements.
        ValueError: If m_a or m_b is empty, or if the matrices can't be multiplied.

    """
    # Validate m_a
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")

    if any(not isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")

    # Validate m_b
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    if any(not isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    # Validate matrix shapes for multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result
