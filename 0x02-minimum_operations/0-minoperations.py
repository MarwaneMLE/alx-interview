#!/usr/bin/python3


def minOperations(n):
    """
    calculates the fewest number of operations needed to result
    in exactly n H characters in the file

    Args:
        n: integer number
    Return: an integer n if impossible to achieve or 0 if not
    """
    nxt = 'H'
    body = 'H'
    op = 0
    while (len(body) < n):
        if n % len(body) == 0:
            op += 2
            nxt = body
            body += body
        else:
            op += 1
            body += nxt
    if len(body) != n:
        return 0
    return op
