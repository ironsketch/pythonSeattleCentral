from random import randint

def Turn():
    # Meats Turn
    play = input('Type rock paper or scissors ')
    play = play.lower()

    # Computers Turn
    compplay = randint(0,2)
    if compplay == 0:
        print('c = rock')
        cplay = 'rock'
    elif compplay == 1:
        print('c = paper')
        cplay = 'paper'
    else:
        print('c = scissors')
        cplay = 'scissors'
        
    return cplay,play

def whoWon(comp,meat):
    if comp == meat:
        print(comp,meat)
        return 0,0
    elif ((comp == 'rock') and (meat == 'paper')) or ((comp == 'paper') and (meat == 'scissors')) or ((comp == 'scissors') and (meat == 'rock')):
        return -1,3
    elif ((comp == 'rock') and (meat == 'scissors')) or ((comp == 'paper') and (meat == 'rock')) or ((comp == 'scissors') and (meat == 'paper')):
        return 3,-1

def gamePlay():
    compPoints = 0
    meatPoints = 0
    while (compPoints < 10) and (meatPoints < 10):
        c,m = Turn()
        comp,meat = whoWon(c,m)
        compPoints += comp
        meatPoints += meat
        print('Meat User', 'Computer Cheater')
        print(meatPoints,'          ',compPoints)


    if compPoints >= 10:
        print('THE COMPUTER HAZ ONE.....')
    elif meatPoints >= 10:
        print('YOU HAVE WONNNNNNNN')

gamePlay()
