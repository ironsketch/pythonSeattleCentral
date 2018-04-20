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
            
def average(times):
    for poop in rollOfDice:
        rollOfDice[poop] /= times


def multiple(n,dice,times):
    for i in range (times):
        runThrough(n,dice)
    average(times)

multiple(1000,2,500)



for item in rollOfDice.items():
    print (item)

counterpoop = 0
for item in rollOfDice.values():
    counterpoop += item

print(counterpoop)

