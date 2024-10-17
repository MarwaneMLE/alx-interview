#!/usr/bin/python3


def minOperations(n):
    """
    calculates the fewest number of operations needed to result
    in exactly n H characters in the file

    Args:
        n: integer number
    Return: an integer n if impossible to achieve or 0 if not
    """
    if n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    return sum(factor_list)
