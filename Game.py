# Game.py

import random

def can_reduce_to_10_or_less(n):
    if n <= 10:
        return True
    if n % 2 == 0 and can_reduce_to_10_or_less(n // 2):
        return True
    if n % 3 == 0 and can_reduce_to_10_or_less(n // 3):
        return True
    if n % 4 == 0 and can_reduce_to_10_or_less(n // 4):
        return True
    return False

numbers_that_can_reduce = [n for n in range(20000, 30001) if n % 12 == 0 and can_reduce_to_10_or_less(n)]

def randomNumbers():
    if not numbers_that_can_reduce:  # Check if the list is empty or None
        return []  # Return an empty list if there's nothing to sample from
    return random.sample(numbers_that_can_reduce, 5)


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
