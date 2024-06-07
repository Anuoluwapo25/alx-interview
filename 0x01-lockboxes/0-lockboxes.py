#!/usr/bin/env python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    """
    jslf
    """
    opened = set()
    # Start with the first box, which is unlocked
    opened.add(0)
    # Iterate through the boxes
    for box in boxes:
        # If the box is already opened, skip it
        if box[0] in opened:
            continue
        # Check if the box can be opened with the keys in the other boxes
        for key in box:
            if key in opened:
                opened.add(box[0])
                break
    # Return True if all boxes are opened, False otherwise
    return len(opened) == len(boxes)
