from random import randint

def flipCoin():
    flip = randint(0,1)
    return flip

def flipCoins(n):
    counter = 0
    for i in range (n):
        flip = flipCoin()
        if flip == 1:
            counter += 1
    return counter

def rollDie():
    roll = randint(1,6)
    return roll

def rollDice(n):
    counter = 0
    for i in range (n):
        roll = rollDie()
        counter += roll
    return counter

def tossAndRoll(n):
    tup = ()
    flip = flipCoins(n)
    roll = rollDice(n)
    tup = flip,roll
    return tup
        
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
