#!/usr/bin/python3
""" This module conatins the makeChange function """
from typing import List
import time


def makeChange(coins: List[int], total: int) -> int:
    if total == 0:
        return 0

    coins.sort(reverse=True)
    for coin in coins:
        if coin > total:
            continue
        # print(f"{total} - {coin}")
        total -= coin
        # time.sleep(3)
        # print(f"TOTAL => {total}")
        total_coins = makeChange(coins, total)
        # print(f"TOTAL COINS => {total_coins}")
        if total_coins == -1:
            total += coin
            # print(f"NEW TOTAL => {total}")
            continue
        total_coins += 1
        return total_coins

    return -1
