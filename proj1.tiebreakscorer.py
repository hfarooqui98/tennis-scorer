def comp101_tiebreaker(points, server):
    '''Takes a list of points and the server whos serving and
    returns the score, winner(if any), extra points(if any)'''
    score = 0
    winner = None
    remainder = []
    iter_points = points.copy()  # copy points to itterate on without mutation
    plyr0scr = 0  # Player 0's running total
    plyr1scr = 0  # Player 1's running total

    # Checking if unstarted game
    if len(points) == 0:
        return ('0-0', None, [])

    # Adding score for plyr0 or plyr1 till one wins, assigning rest to remainder
    for count in points:
        if count == 0:
            plyr0scr += 1
        else:
            plyr1scr += 1
        iter_points.pop(0)

        # Checking to break count if minimum winning score achieved
        if (plyr0scr >= 7) or (plyr1scr >= 7):
            if plyr1scr <= (plyr0scr-2):
                break
            elif plyr0scr <= (plyr1scr-2):
                break
        remainder = iter_points

    # Checking whose score should print first
    score0 = ('{}-{}').format(plyr0scr, plyr1scr)
    score1 = ('{}-{}').format(plyr1scr, plyr0scr)
    if server == 0:
        score = score0
    else:
        score = score1

    # Checking for winner
    if (plyr0scr >= 7) or (plyr1scr >= 7):
        if plyr1scr <= (plyr0scr-2):
            winner = 0
        elif plyr0scr <= (plyr1scr-2):
            winner = 1
        else:
            winner = None
    else:
        winner = None
    return (score, winner, remainder)
