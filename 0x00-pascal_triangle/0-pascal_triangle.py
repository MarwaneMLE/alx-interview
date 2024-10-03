#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """
    Pascal triangle method

    Args:
        n(int): integer determine te size of triange

    Returns:
        list of integers representing the Pascal Triangle of n
        returns empty list if n <= 0
    """

    K = []

    if n <= 0:
        return K

    K = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(K[i-1])-1):
            current = K[i-1]
            temp.append(K[i-1][j] + K[i-1][j+1])
        temp.append(1)
        K.append(temp)
    return K
