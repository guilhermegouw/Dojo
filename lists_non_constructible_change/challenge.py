"""
Given an array of positive integers representing the values of coins in your
possession, write a function that returns the minimum amount of
change(the minimum sum of money) that you cannot create. The given can have any
positive integer value and aren't necessarily unique(you can have multiple
coins of the same value).

Example:

If you were given coins = [1, 2, 5], the minimum amount of change that you
can't create is 4. If you were given no coins, the minimum amount of change
that you can't create is 1.

Input:

coins = [5, 7, 1, 1, 2, 3, 22]

Output:

20
"""


def non_constructible_change(coins):
    sorted_coins = sorted(coins)
    current_change = 0
    for coin in sorted_coins:
        if coin > current_change + 1:
            return current_change + 1
        current_change += coin
    return current_change + 1
