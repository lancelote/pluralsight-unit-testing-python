# coding=utf-8

""""
Yatzy Game
"""

from operator import itemgetter


def dice_counts(dice):
    """Make a dictionary of how many of each value are in the dice

    Args:
        dice (lst): A sorted list of 5 integers indicating the dice rolled

    Returns:
        dict: How many of each value are in the dice

    Examples:
        >>> sorted(dice_counts([1, 2, 2, 3, 3]).items())
        [(1, 1), (2, 2), (3, 2), (4, 0), (5, 0), (6, 0)]
        >>> dice_counts('12345')
        Traceback (most recent call last):
            ...
        TypeError: Can't convert 'int' object to str implicitly
    """
    return {x: dice.count(x) for x in range(1, 7)}


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


def yatzy(dice):
    """Score the given roll in the 'Yatzy' category

    Args:
        dice (list): A sorted list of 5 integers indicating the dice rolled

    Returns:
        int: Score

    Examples:
        >>> yatzy([1, 1, 1, 1, 1])
        50
        >>> yatzy([4, 4, 4, 4, 4])
        50
        >>> yatzy([4, 4, 4, 4, 1])
        0
    """
    counts = dice_counts(dice)
    if 5 in counts.values():
        return 50
    return 0


def full_house(dice):
    """Score the given roll in the 'Full House' category

    Args:
        dice (list): A sorted list of 5 integers indicating the dice rolled

    Returns:
        int: Score

    Examples:
        >>> full_house([1, 1, 2, 2, 2])
        8
        >>> full_house([6, 6, 6, 2, 2])
        22
        >>> full_house([1, 2, 3, 4, 5])
        0
        >>> full_house([1, 2, 2, 1, 3])
        0
    """
    counts = dice_counts(dice)
    if 2 in counts.values() and 3 in counts.values():
        return sum(dice)
    return 0


def ones(dice):
    """Scores the given roll in the 'Ones' category

    Args:
        dice (list): A sorted list of 5 integers indicating the dice rolled

    Returns:
        int: Score
    """
    return dice_counts(dice)[1]


def twos(dice):
    """Scores the given roll in the 'Twos' category

    Args:
        dice (list): A sorted list of 5 integers indicating the dice rolled

    Returns:
        int: Score
    """
    return dice_counts(dice)[2]*2

ALL_CATEGORIES = [full_house, yatzy, small_straight, ones, twos]


def scores_in_categories(dice, categories=ALL_CATEGORIES):
    """Score the dice in each category and return those with a non-zero score

    Args:
        dice (list): A sorted list of 5 integers indicating the dice rolled
        categories (list): A list of category functions

    Returns:
        list: Category scores

    Examples:
        >>> scores = scores_in_categories([1, 1, 2, 2, 2])
        >>> [(score, category.__name__) for (score, category) in scores]
        [(8, 'full_house'), (6, 'twos'), (2, 'ones')]
    """
    scores = [(category(dice), category) for category in categories
              if category(dice) > 0]
    return sorted(scores, reverse=True, key=itemgetter(0))
