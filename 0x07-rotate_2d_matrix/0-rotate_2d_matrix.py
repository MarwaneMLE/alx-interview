#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Method that rotate 2D matrix to 90 degrees clockwise
    
    Args:
        matrix: 2D matrix
    """
    matrix.reverse()
    length = len(matrix)
    for i in range(length):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
