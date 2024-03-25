# Game.py

import random
from graphics import endGameScreen


def scoreUpdate(divisor):
    global humanPoints, aiPoints, bankPoints, isPlayersTurn, chosenNumber
    result = chosenNumber / divisor

    if result % 2 == 0:
        if isPlayersTurn:
            humanPoints -= 1
        else:
            aiPoints -= 1
    else:
        if isPlayersTurn:
            humanPoints += 1
        else:
            aiPoints += 1

    if result % 10 == 0:
        bankPoints += 1

    chosenNumber = result  # Update the chosenNumber with the result of the division
    return result

def gameOver():
    global humanPoints, aiPoints, bankPoints, isPlayersTurn, chosenNumber
    # Game ends when the chosen number is below or the same as 10
    if chosenNumber <= 10:
        if isPlayersTurn:
            humanPoints += bankPoints
        else:
            aiPoints += bankPoints
        endGameScreen()  # Call the end game screen
        return True

    # Game ends if there are no more legal moves left
    legal_moves = [chosenNumber % div == 0 for div in [2, 3, 4]]
    if not any(legal_moves):
        # It's a draw, distribute bank points according to your game rules
        # Example: split the bank points
        humanPoints += bankPoints // 2
        aiPoints += bankPoints // 2
        endGameScreen()  # Call the end game screen
        return True
    
    return False
