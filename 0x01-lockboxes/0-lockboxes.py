#!/usr/bin/python3
"""
    Create a function that determines if all the boxes can be opened.

    return: True or False
"""


def canUnlockAll(boxes):
    """
        a method that determines if all the boxes can be opened.

        return: True or False
    """
    if len(boxes) == 0:
        return False

    keys = {0}

    visited = set()

    stack = [0]

    while stack:
        box = stack.pop()
        visited.add(box)

        for key in boxes[box]:
            keys.add(key)
            if key not in visited:
                stack.append(key)

    return len(visited) == len(boxes)
