#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""


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
    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False
