SCORE_NAMES = ('Love', 'Fifteen', 'Thirty', 'Forty')


def tennis_score(player1, player2):
    if player1 == player2:
        return '%s-All' % SCORE_NAMES[player1]
    else:
        return '%s-%s' % (SCORE_NAMES[player1], SCORE_NAMES[player2])
