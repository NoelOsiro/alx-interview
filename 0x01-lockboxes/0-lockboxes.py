#!/usr/bin/python3
from collections import deque


def canUnlockAll(boxes):
    """Determine if all boxes can be opened.

    Args:
        boxes (list of list): A list of lists representing the boxes.
            Each box is represented by a list containing the indices
            of the boxes it can unlock.

    Returns:
        bool: True if all boxes can be opened, False otherwise.

    Examples:
        >>> boxes1 = [[1], [2], [3], [4], []]
        >>> canUnlockAll(boxes1)
        True

    """
    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False
    return True
