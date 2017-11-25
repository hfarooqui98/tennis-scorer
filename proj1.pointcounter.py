def comp101_score(points, player):
    '''Returns score of the player followed by score of opponent'''
    plyr1scr = 0  # Player 0's score
    plyr2scr = 0  # Player 1's score

# Adding score for plyr1 or plyr2
    for count in points:
        if count == 0:
            plyr1scr += 1
        else:
            plyr2scr += 1

# Checking whose score should print first
    score0 = (plyr1scr, plyr2scr)
    score1 = (plyr2scr, plyr1scr)
    if player == 0:
        return score0
    else:
        return score1
