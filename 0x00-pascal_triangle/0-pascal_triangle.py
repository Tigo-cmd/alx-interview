#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n: int):
    """
    this function prints out the pascal's triangle sequence

    :param n: an integer to determine the pascal triangle
    :return: Returns an empty list if n <= 0
    """
    numbers = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        previous = numbers[-1]
        new = [1]
        for j in range(1, len(previous)):
            new.append(previous[j - 1] + previous[j])

        new.append(1)

        numbers.append(new)

    return numbers
