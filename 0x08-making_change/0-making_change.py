#!/usr/bin/python3
"""Change making module interview question.
"""


def makeChange(coins, total):
    """Calculates the minimum number of coins required to achieve a specified 
      total amount, given a collection of coins with varying denominations.
    """
    if total <= 0:
        return 0
    remains = total
    coinsCount = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remains > 0:
        if coin_index >= n:
            return -1
        if remains - sorted_coins[coin_index] >= 0:
            remains -= sorted_coins[coin_index]
            coinsCount += 1
        else:
            coin_index += 1
    return coinsCount
