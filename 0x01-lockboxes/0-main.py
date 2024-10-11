#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

# boxes = [[1, 2], [2], [3], [4], []]
# print(canUnlockAll(boxes))

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes))

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes))

boxes = [[], [], [], [], []]
print(f'EXPECTED: False --- Returned -> {canUnlockAll(boxes)}')

boxes = [[1], [0], [3], [], []]
print(f'EXPECTED: False --- Returned -> {canUnlockAll(boxes)}')

boxes = [[1, 2, 3], [], [], [], []]
print(f'EXPECTED: False --- Returned -> {canUnlockAll(boxes)}')

boxes = [[1, 3], [2, 4], [], [], []]
print(f'EXPECTED: True --- Returned -> {canUnlockAll(boxes)}')

boxes = [[1, 4], [2], [], [], [3]]
print(f'EXPECTED: True --- Returned -> {canUnlockAll(boxes)}')

# Key that doesn't exist
boxes = [[1, 4], [2], [5], [], [3]]
print(f'EXPECTED: True --- Returned -> {canUnlockAll(boxes)}')

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(f'EXPECTED: False --- Returned -> {canUnlockAll([0, [2]])}')

boxes = [[], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(f'EXPECTED: False --- Returned -> {canUnlockAll([0, [2]])}')

boxes = None
print(f'EXPECTED: False --- Returned -> {canUnlockAll([0, [2]])}')