#!/usr/bin/python3
""" This module contains the minOperation function """


def minOperations(n: int) -> int:
    """
    :param n: The desired number of 'H' characters.
    :return: The minimum number of operations to achieve exactly
        n 'H' characters.
    """
    operation_count = 0

    # Start with the smallest divisor (2) and work upwards
    divisor = 2

    while n > 1:
        # If n is divisible by the current divisor
        while n % divisor == 0:
            operation_count += divisor
            n //= divisor
        # Try the next potential divisor
        divisor += 1

    return operation_count
