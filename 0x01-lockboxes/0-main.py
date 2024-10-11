#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

# boxes = [[1, 2], [2], [3], [4], []]
# print(canUnlockAll(boxes))

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes))

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes))

# boxes = [[], [], [], [], []]
# print(f'EXPECTED: False --- Returned -> {canUnlockAll(boxes)}')

# boxes = [[1], [0], [3], [], []]
# print(f'EXPECTED: False --- Returned -> {canUnlockAll(boxes)}')

# boxes = [[1, 2, 3], [], [], [], []]
# print(f'EXPECTED: False --- Returned -> {canUnlockAll(boxes)}')

# boxes = [[1, 3], [2, 4], [], [], []]
# print(f'EXPECTED: True --- Returned -> {canUnlockAll(boxes)}')

# boxes = [[1, 4], [2], [], [], [3]]
# print(f'EXPECTED: True --- Returned -> {canUnlockAll(boxes)}')

# Key that doesn't exist
boxes = [[1, 1, 8], [2], [5, 4], [], [3]]
print(f'EXPECTED: True --- Returned -> {canUnlockAll(boxes)}')

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(f'EXPECTED: False --- Returned -> {canUnlockAll(boxes)}')

boxes = [None, [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(f'EXPECTED: False --- Returned -> {canUnlockAll(boxes)}')

# boxes = None
# print(f'EXPECTED: False --- Returned -> {canUnlockAll(boxes)}')


boxes = []
keys = []
for n in range(1, 1000):
  keys = []
  for m in range(1, 1000):
    keys.append(m)
  boxes.append(keys)
print(boxes)
print(canUnlockAll(boxes))
  