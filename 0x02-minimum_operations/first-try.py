#!/usr/bin/python3
"""This module contains the minOperations function."""


def minOperations(target: int) -> int:
    """
    The function works by finding the largest divisor of 'target' and
    recursively calculating the operations for that divisor.

    :param target: The desired number of 'H' characters.
    :return: The minimum number of operations to achieve exactly
        'target' 'H' characters.
    """
    # Initialize total_operations to store the number of operations required
    total_operations = 0

    # Start by checking divisors from (target - 1) downwards
    divisor = target - 1

    while divisor > 1:
        if target % divisor == 0:
            # Calculate the number of operations by dividing
            # the target by the divisor
            total_operations += target // divisor

            # Recursively find the minimum operations for the divisor
            while True:
                # Recursively call minOperations to handle the divisor
                next_operations = minOperations(divisor)

                # Add the result from the recursive call to total_operations
                total_operations += next_operations

                # If the recursive call returned a valid result, break the loop
                if next_operations:
                    break
            break

        # Decrease the divisor to check the next possible divisor
        divisor -= 1

    # If no divisors were found, the target is prime,
        # so return the target itself
    if total_operations == 0:
        total_operations = target

    return total_operations
