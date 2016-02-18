# coding=utf-8

""""
Yatzy Game
"""


def small_straight(dice):
    """Score the given roll in the 'Small Straight' Yatzy category

    Args:
        dice (lst): A sorted list of 5 integers indicating the dice rolled

    Returns:
        int: Score

    Examples:
        >>> small_straight([1, 2, 3, 4, 5])
        15
        >>> small_straight([1, 2, 3, 4, 4])
        0

        This function works with lists or sets or other collection types:

        >>> small_straight({1, 2, 3, 4, 5})
        15
        >>> small_straight([5, 4, 3, 2, 1])
        15
    """
    return sum(dice) if sorted(dice) == [1, 2, 3, 4, 5] else 0
