# Import the pre-implemented versions of Q1 and Q2 functions.
from hidden_lib import comp101_game, comp101_tiebreaker


def comp101_set(points, server, tiebreaker = comp101_tiebreaker, game = comp101_game):
    '''Takes a list of points and who is serving and returns final set score,
    who won the set(if anyone), and score score remaining(if any)'''
    plyr0gmscr = 0
    plyr1gmscr = 0
    winner = None
    remainder = []
    iter_remainder = points.copy()
    score = ''

    # Checking if unstarted game
    if len(points) == 0:
        return ('0-0', None, [])

    # Counting games won by plyr0/1 upto 6 wins, if achieved
    while (remainder != iter_remainder) and (plyr1gmscr != 6 and plyr0gmscr != 6):
        game_score = game(iter_remainder, 0)
        if 'W' in game_score[0][0]:
            plyr0gmscr += 1
            remainder = iter_remainder.copy()
            iter_remainder = game_score[2]
        elif 'W' in game_score[0][2:]:
            plyr1gmscr += 1
            remainder = iter_remainder.copy()
            iter_remainder = game_score[2]
        else:
            break

    # Checking for Winner
    if (plyr0gmscr < 6) and (plyr1gmscr < 6):
        winner = None
    elif plyr1gmscr <= 4:
        winner = 0
    elif plyr0gmscr <= 4:
        winner = 1

    # In case game score is 6-5, play another match
    elif plyr1gmscr == 5 or plyr0gmscr == 5:
        game_extra = game(iter_remainder, 0)
        if 'W' in game_extra[0][0]:
            plyr0gmscr += 1
            iter_remainder = game_extra[2]
            winner = 0
        elif 'W' in game_extra[0][2:]:
            plyr1gmscr += 1
            iter_remainder = game_extra[2]
            winner = 1
        else:
            winner = None

    # In case game score is 6-6, tiebreaker game played
    if (plyr0gmscr == plyr1gmscr) and (plyr0gmscr == 6):
        tiebreaker_score = tiebreaker(iter_remainder, 0)
        if tiebreaker_score[0][0] > tiebreaker_score[0][2]:
            plyr0gmscr += 1
            iter_remainder = tiebreaker_score[2]
            winner = 0
        elif tiebreaker_score[0][2] > tiebreaker_score[0][0]:
            plyr1gmscr += 1
            iter_remainder = tiebreaker_score[2]
            winner = 1
        else:
            winner = None

    # Checking whos score prints first
    if server == 0:
        score = '{}-{}'.format(plyr0gmscr, plyr1gmscr)
    else:
        score = '{}-{}'.format(plyr1gmscr, plyr0gmscr)
    if winner is None:
        remainder = []
    else:
        remainder = iter_remainder
    return (score, winner, remainder)
