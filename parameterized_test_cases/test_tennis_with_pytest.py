import pytest

from .tennis import tennis_score


EXAMPLES = (
    ('expected', 'player1', 'player2', 'comment'),
    [
        ('Love-All', 0, 0, 'early game, scores equal'),
        ('Fifteen-All', 1, 1, 'early game, scores equal'),
        ('Thirty-All', 2, 2, 'early game, scores equal'),
        ('Love-Fifteen', 0, 1, 'early game, uneven scores'),
        ('Fifteen-All', 1, 1, 'early game, uneven scores'),
        ('Thirty-Fifteen', 2, 1, 'early game, uneven scores'),
        ('Forty-Thirty', 3, 2, 'early game, uneven scores'),
        ('Advantage Player 1', 4, 3, 'endgame, with uneven scores'),
        ('Advantage Player 1', 23, 22, 'endgame, with uneven scores'),
        ('Deuce', 4, 4, 'endgame, with even scores'),
        ('Deuce', 3, 3, 'endgame, with even scores'),
        ('Deuce', 14, 14, 'endgame, with even scores'),
        ('Win for Player 1', 4, 0, 'endgame, with winner'),
        ('Win for Player 2', 1, 4, 'endgame, with winner'),
        ('Win for Player 1', 6, 4, 'endgame, with winner')
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_early_game_scores_equal(expected, player1, player2, comment):
    assert expected == tennis_score(player1, player2), comment


def test_early_game_scores_equal_ordinary():
    """None parametrized version"""
    assert 'Love-All' == tennis_score(0, 0)
    assert 'Fifteen-All' == tennis_score(1, 1)
    assert 'Thirty-All' == tennis_score(2, 2)
