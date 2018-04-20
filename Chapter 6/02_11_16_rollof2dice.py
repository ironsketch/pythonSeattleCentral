from random import randint

rollOfDice = {}

def randRoll(dice):
    counter = 0
    for i in range(dice):
        randNum = randint(1,6)
        counter += randNum
    return counter

def runThrough(n,dice):
    for i in range(n):
        poop = randRoll(dice)
        if poop in rollOfDice:
            rollOfDice[poop] += 1
        else:
            rollOfDice[poop] = 1

runThrough(1000,5)
for item in rollOfDice.items():
    print (item)
