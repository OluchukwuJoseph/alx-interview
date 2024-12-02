#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(f"RETURN VALUE => {makeChange([1, 2, 25], 37)}")

print(f"RETURN VALUE => {makeChange([1256, 54, 48, 16, 102], 1453)}")
print(f"RETURN VALUE => {makeChange([5, 4], 13)}")
print(f"RETURN VALUE => {makeChange([4, 3], 5)}")
print(f"RETURN VALUE => {makeChange([4, 3, 2], 1)}")
