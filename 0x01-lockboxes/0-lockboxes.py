#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened.
    Args:
        boxes: list of lists
    Return: True if all boxes can be opened, else return Falss
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for i in range(1, len(boxes) - 1):
        boxes_checked = False
        for indx in range(len(boxes)):
            boxes_checked = i in boxes[indx] and i != indx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
