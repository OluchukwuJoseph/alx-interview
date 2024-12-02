#!/usr/bin/python3
""" This module conatins the makeChange function """
from typing import List
import time


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
    # Initialize dp array with max value (total + 1)
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make 0
    dp[0] = 0

    # Compute minimum coins for each amount from 1 to total
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return -1 if no solution found, otherwise return minimum coins
    return dp[total] if dp[total] != float('inf') else -1
