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


def scoreUpdate(number, devisor):
  global humanPoints, aiPoints, bankPoints, isPlayerTurn
  result = number / devisor

  if result % 2 :
    if isPlayerTurn:
      humanPoints -= 1
    else:
      aiPoints -= 1
  else:
    if isPlayerTurn:
      humanPoints += 1
    else:
      aiPoints += 1

  if result % 10 == 0:
    bankPoints += 1

  return result
