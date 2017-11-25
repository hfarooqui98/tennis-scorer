def comp101_game(points, server):
    '''Takes a list of points and the server whos serving and
    returns the score, winner(if any), extra points(if any)'''
    score = 0
    winner = None
    remainder = []
    iter_points = points.copy()  # copy points to itterate on without mutation
    plyr0scr = 0  # Player 0's running total
    plyr1scr = 0  # Player 1's running total
    tenis_dict = {0: '0', 1: '15', 2: '30', 3: '40', 4: 'Ad', 5: 'W'}

    # Checking if unstarted game
    if len(points) == 0:
        return ('0-0', None, [])

    # Add scores for plyr0/1 till win or str end,assign leftover to remainder
    # Initiating a running count of scores
    for count in points:
        if count == 0:
            plyr0scr += 1
        else:
            plyr1scr += 1
        iter_points.pop(0)
        if (plyr0scr >= 4) or (plyr1scr >= 4):

            # Win plyr0
            if plyr1scr <= (plyr0scr-2):
                plyr0scr = 5
                plyr0scr, plyr1scr = tenis_dict[plyr0scr], tenis_dict[plyr1scr]
                break

            # Win plyr1
            elif plyr0scr <= (plyr1scr-2):
                plyr1scr = 5
                plyr0scr, plyr1scr = tenis_dict[plyr0scr], tenis_dict[plyr1scr]
                break

            # Advantage plyr0
            elif plyr1scr == (plyr0scr-1):
                plyr0scr = 4
                plyr1scr = 3

            # Advantage plyr1
            elif plyr0scr == (plyr1scr-1):
                plyr1scr = 4
                plyr0scr = 3

            # Duce
            elif (plyr0scr == 4) and (plyr1scr == 4):
                plyr0scr = 3
                plyr1scr = 3

    remainder = iter_points

    # Final assignment for 'score' with "Tenis Scoring Scale"

    # Duce and advantage scenarios
    if type(plyr1scr) is float:
        plyr0scr, plyr1scr = tenis_dict[plyr0scr], tenis_dict[plyr1scr]
        if server == 0:
            score = ('{}-{}').format(plyr0scr, plyr1scr)
        else:
            score = ('{}-{}').format(plyr1scr, plyr0scr)

    # No duce/adv
    elif (type(plyr1scr) is int) and (type(plyr0scr) is int):
        plyr0scr, plyr1scr = tenis_dict[plyr0scr], tenis_dict[plyr1scr]
        if server == 0:
            score = ('{}-{}').format(plyr0scr, plyr1scr)
        else:
            score = ('{}-{}').format(plyr1scr, plyr0scr)
    else:
        if server == 0:
            score = ('{}-{}').format(plyr0scr, plyr1scr)
        else:
            score = ('{}-{}').format(plyr1scr, plyr0scr)

    # Assignment of 'winner' variable
    if 'W' in score:
        if plyr0scr == 'W':
            winner = 0
        else:
            winner = 1
    return (score, winner, remainder)
