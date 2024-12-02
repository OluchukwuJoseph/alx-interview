#!/usr/bin/python3
""" This module conatins the makeChange function """
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Determines the fewest number of coins needed to meet a given amount.

    Args:
        coins (list): A list of coin denominations available.
        total (int): The target amount of money.

    Returns:
        int: The minimum number of coins needed to achieve the total,
             or -1 if it is not possible.
    """
    # If total is less than 1 return -1
    if total <= 0:
        return -1

    # Initialize dp array with max value (total + 1)
    memory = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make 0
    memory[0] = 0

    # Compute minimum coins for each amount from 1 to total
    for item in range(1, total + 1):
        for coin in coins:
            if coin <= item:
                sub_problem = item - coin
                memory[item] = min(memory[sub_problem] + 1, memory[item])

    # Return -1 if no solution found, otherwise return minimum coins
    return memory[total] if memory[total] != float('inf') else -1
