from random import randint

rollOfDice = {1:0,2:0,3:0,4:0,5:0,6:0}
randNum = randint(1,6)

def randRoll():
    randNum = randint(1,6)
    return randNum

def runThrough(n):
    for i in range(n):
        rollOfDice[randRoll()] += 1
        
def addAll():
    counter = 0
    for num in rollOfDice.values():
        counter += num
    return counter

def frequency():
    counter = 1
    for num in rollOfDice.values():
        a = 0
        a = (num / 1000) * 100
        print(counter,' = %',a)
        counter += 1
        
runThrough(1000)

print(rollOfDice)
print(addAll())
frequency()
