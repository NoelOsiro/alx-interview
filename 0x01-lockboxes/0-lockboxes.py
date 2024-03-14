#!/usr/bin/python3
from collections import deque


def can_unlock_all(boxes):
    # Initialize a set to keep track of encountered keys
    keys = set()
    # Initialize a queue with the first box
    queue = deque([0])

    # Loop until the queue is empty
    while queue:
        # Pop the first box from the queue
        box = queue.popleft()
        # Add the keys from the current box to the set of keys
        keys.update(boxes[box])
        # Add the boxes that can be unlocked with the keys to the queue
        for key in boxes[box]:
            if key < len(boxes) and key not in keys:
                queue.append(key)

    # Check if all boxes can be opened
    return len(keys) == len(boxes)
