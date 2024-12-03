#!/usr/bin/python3
'''A module for working with lockboxes in alx interview.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    seen = set([0])
    not_seen = set(boxes[0]).difference(set([0]))
    while len(not_seen) > 0:
        boxIndex = not_seen.pop()
        if not boxIndex or boxIndex >= n or boxIndex < 0:
            continue
        if boxIndex not in seen:
            not_seen = not_seen.union(boxes[boxIndex])
            seen.add(boxIndex)
    return n == len(seen)
