#!/usr/bin/python3
"""Prime"""


def isWinner(x, nums):
    """
    winner
    """
    mariaWins = 0
    benWins = 0

    for num in nums:
        primeCount = countPrimes(num)
        if primeCount % 2 == 0:
            benWins += 1
        else:
            mariaWins += 1

    if mariaWins > benWins:
        return "Maria"
    elif mariaWins < benWins:
        return "Ben"
    else:
        return None


def countPrimes(number):
    """
    number for a players
    """
    count = 0
    for i in range(2, number + 1):
        if isPrimeNumber(i):
            count += 1
    return count


def isPrimeNumber(number):
    """
    returns False
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
