#!/usr/bin/env python3
""" This module contains the `isWinner` function """


def find_prime_numbers(candidate_numbers):
    """
    Find prime numbers within a given list of numbers
        using the Sieve of Eratosthenes algorithm.

    This function efficiently identifies prime numbers by
        eliminating multiples of prime numbers.
    It handles edge cases and works with positive integers.

    Args:
        candidate_numbers (list): A list of positive integers
            to check for prime numbers.

    Returns:
        list: A sorted list of prime numbers found within the candidate numbers
    """
    # Special case for numbers less than 2
    if not candidate_numbers or max(candidate_numbers) < 2:
        return []

    # Use a more efficient Sieve of Eratosthenes approach
    max_number = max(candidate_numbers)
    sieve = [True] * (max_number + 1)
    sieve[0] = sieve[1] = False

    # Mark non-prime numbers
    for current_prime in range(2, int(max_number**0.5) + 1):
        if sieve[current_prime]:
            # Mark multiples of current prime as non-prime
            for multiple in range(current_prime * current_prime,
                                  max_number + 1, current_prime):
                sieve[multiple] = False

    # Collect prime numbers that are within the candidate list
    prime_numbers = [num for num in range(2, max_number + 1)
                     if sieve[num] and num in candidate_numbers]

    return prime_numbers


def isWinner(x, nums):
    """
    Determine the winner of a prime number game based on specific rules.

    The game is played with multiple rounds. In each round:
    - A list of numbers from 1 to n is generated
    - Prime numbers in this list are counted
    - If the count of prime numbers is even, Ben wins
    - If the count of prime numbers is odd, Maria wins

    Args:
        x (int): Number of rounds to play
        nums (list): List of numbers representing each round's upper limit

    Returns:
        str: The name of the winner ('Maria' or 'Ben'),
            or None if input is invalid
    """
    # Input validation
    if (not isinstance(x, int) or not isinstance(nums, list)):
        return None
    if (x <= 0 or len(nums) == 0):
        return None

    # Track wins for Maria and Ben
    game_results = [0, 0]

    # Play each round
    for round_limit in nums:
        round_numbers = list(range(1, round_limit + 1))
        prime_count = len(find_prime_numbers(round_numbers))

        # Determine round winner based on prime number count
        if prime_count % 2 == 0:
            game_results[1] += 1  # Ben wins
        else:
            game_results[0] += 1  # Maria wins

    # Determine overall winner
    return 'Maria' if game_results[0] > game_results[1] else 'Ben'
