#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    ops = 0
    clip = 0
    success = 1
    while success < n:
        if clip == 0:
            clip = success
            success += clip
            ops += 2
        elif n - success > 0 and (n - success) % success == 0:
            clip = success
            success += clip
            ops += 2
        elif clip > 0:
            success += clip
            ops += 1
    return ops
