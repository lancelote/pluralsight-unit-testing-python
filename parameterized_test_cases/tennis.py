SCORE_NAMES = ('Love', 'Fifteen', 'Thirty', 'Forty')


def tennis_score(player1, player2):
    if player1 == player2:
        if player1 > 2:
            return 'Deuce'
        else:
            return '%s-All' % SCORE_NAMES[player1]
    elif abs(player1 - player2) > 1 and (player1 > 3 or player2 > 3):
        return 'Win for Player %d' % (1 if player1 > player2 else 2)
    else:
        if player1 + player2 > 6:
            return 'Advantage Player %d' % (1 if player1 > player2 else 2)
        else:
            return '%s-%s' % (SCORE_NAMES[player1], SCORE_NAMES[player2])
