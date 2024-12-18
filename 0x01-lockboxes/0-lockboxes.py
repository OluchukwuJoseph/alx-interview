#!/usr/bin/python3
"""
    This module contains canUnlockAll function which
    determines if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked starting from the first box

    Parameters:
    boxes (list of lists): A list where each element is a list of keys
    that unlock other boxes.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    if not boxes or not isinstance(boxes, list) or len(boxes) == 0:
        return False

    for box in boxes:
        if not isinstance(box, list):
            return False

    # Queue to track which boxes and their contents (keys) we need to process
    queue = [(0, boxes[0])]
    # List to track visited (unlocked) boxes
    visited = []

    while len(queue) > 0:
        # Extract the current box's keys and its index from the queue
        currentBoxKeys = queue[0][1]
        currentBoxIndex = queue[0][0]

        # If the current box has already been visited,
        # remove it from the queue and continue
        if currentBoxIndex in visited:
            queue.remove(queue[0])
            continue

        # Mark the current box as visited (unlocked)
        visited.append(currentBoxIndex)
        queue.remove(queue[0])

        for key in currentBoxKeys:
            if key >= len(boxes):
                continue
            queue.append((key, boxes[key]))
        if len(visited) == len(boxes):
            return True

    return False
