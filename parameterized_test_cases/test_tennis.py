import unittest

from .tennis import tennis_score

TEST_CASE_DATA = {
    'even_scores': [
        ('Love-All', 0, 0),
        ('Fifteen-All', 1, 1),
        ('Thirty-All', 2, 2)
    ],
    'early_games_with_uneven_scores': [
        ('Love-Fifteen', 0, 1),
        ('Fifteen-Love', 1, 0),
        ('Love-Thirty', 0, 2),
        ('Forty-Thirty', 3, 2)
    ],
    'endgame_with_uneven_scores': [
        ('Advantage Player 1', 4, 3),
        ('Advantage Player 2', 5, 6),
        ('Advantage Player 1', 13, 12)
    ],
    'endgame_with_even_scores': [
        ('Deuce', 3, 3),
        ('Deuce', 4, 4),
        ('Deuce', 14, 14)
    ],
    'there_is_a_winner': [
        ('Win for Player 1', 4, 0),
        ('Win for Player 2', 2, 4),
        ('Win for Player 1', 6, 4)
    ]
}


def tennis_test_template(*args):
    def foo(self):
        self.assert_tennis_score(*args)
    return foo


class TennisTest(unittest.TestCase):

    def assert_tennis_score(self, expected_score, score1, score2):
        self.assertEqual(expected_score, tennis_score(score1, score2))

for behaviour, test_cases in TEST_CASE_DATA.items():
    for tennis_test_case_data in test_cases:
        expected_output, player1, player2 = tennis_test_case_data
        test_name = 'test_%s_%s_%s' % (behaviour, player1, player2)
        tennis_test_case = tennis_test_template(*tennis_test_case_data)
        setattr(TennisTest, test_name, tennis_test_case)
