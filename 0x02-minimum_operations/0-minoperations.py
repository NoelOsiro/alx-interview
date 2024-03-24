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
    if n <= 1:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):  # Optimize loop bounds
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
