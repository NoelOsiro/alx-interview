#!/usr/bin/python3

"""
Document Module: minOperations

This module defines a function minOperations(n)
that calculates the minimum number of operations
needed to achieve a certain number of 'H' characters
in a text file using copy and paste operations.

Args:
    n (int): The desired number of 'H' characters.

Returns:
    int: The minimum number of operations required.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to achieve a
    certain number of 'H' characters.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required.
    """
    ops = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            ops += min_operations
            n /= min_operations
        min_operations += 1
    return ops
