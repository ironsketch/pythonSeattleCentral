# Importing random
from random import randint

# Using random to pick a number 1 or 0
def flipCoin():
    flip = randint(0,1)
    return flip

# Using flipCoin multiple times and adding up the total of heads
def flipCoins(n):
    counter = 0
    for i in range (n):
        flip = flipCoin()
        if flip == 1:
            counter += 1
    return counter

# Using random to pick a number 1 - 6
def rollDie():
    roll = randint(1,6)
    return roll

# Using rollDie multiple times and adding up the dice total
def rollDice(n):
    counter = 0
    for i in range (n):
        roll = rollDie()
        counter += roll
    return counter

# Using the previous functions to create a tuple of the results
# side by side
def tossAndRoll(n):
    tup = ()
    flip = flipCoins(n)
    roll = rollDice(n)
    tup = flip,roll
    return tup

# Finally putting them into a dictionary to see the frequency of each
# Toss and roll together
def tossAndRollRepeat(n,m):
    both = {}
    for i in range (m):
        tup = tossAndRoll(n)
        if tup in both:
            both[tup] += 1
        else:
            both[tup] = 1
    print(both)

tossAndRollRepeat(5,500)
