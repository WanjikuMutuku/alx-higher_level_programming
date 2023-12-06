#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row for the result_matrix with squared values
        squared_row = [elem ** 2 for elem in row]

        # Append the squared_row to the result_matrix
        result_matrix.append(squared_row)

    return result_matrix
