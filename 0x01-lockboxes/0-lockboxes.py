from collections import deque

def canUnlockAll(boxes):
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

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
