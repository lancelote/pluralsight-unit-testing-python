import unittest

from .tennis import tennis_score


class TennisTest(unittest.TestCase):

    def assert_tennis_score(self, expected_score, player1, player2):
        self.assertEqual(expected_score, tennis_score(player1, player2))

    def test_even_scores_early_game(self):
        self.assert_tennis_score('Love-All', 0, 0)
        self.assert_tennis_score('Fifteen-All', 1, 1)
        self.assert_tennis_score('Thirty-All', 2, 2)

    def test_early_game_with_uneven_scores(self):
        self.assert_tennis_score('Love-Fifteen', 0, 1)
        self.assert_tennis_score('Fifteen-Love', 1, 0)
        self.assert_tennis_score('Love-Thirty', 0, 2)
        self.assert_tennis_score('Forty-Thirty', 3, 2)
