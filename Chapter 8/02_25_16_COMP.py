from random import randint

def randNum(num,num2):
    num = randint(num,num2)
    return num

def rollme():
    roll1 = randNum(1,6)
    roll2 = randNum(1,6)
    added = roll1 + roll2
    return added

def main():
    score = 102
    userRoll = 13
    random = randNum(2,12)
    rolls = []
    while userRoll != random:
        userRoll = rollme()
        rolls.append(userRoll)
        score -= 2

# rolls.append((roll1,roll2))

    print('The rolls were:')
    print(rolls)
    print('The dice was rolled,',len(rolls),'times.')
    print('The secret roll was,',random)
    print('The arbitrary score is,',score)

main()
