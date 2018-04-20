from math import *
from random import randint

def compTurn():
    play = randint(0,2)
    if play == 0:
        print('rock')
        return 'rock'
    if play == 1:
        print('paper')
        return 'paper'
    else:
        print('scissors')
        return 'scissors'

def Turn():
    play = input('Type rock paper or scissors ')
    play = play.lower()
    compplay = randint(0,2)
    if compplay == 0:
        cplay = 'rock'
    elif compplay == 1:
        cplay = 'paper'
    else:
        cplay = 'scissors'
    return cplay,play

def whoWon(comp,meat):
    zero = 0
    negOne = -1
    three = 3
    if comp == meat:
        return zero,zero
    elif ((comp == 'rock') and (meat == 'paper')) or ((meat == 'rock') and (comp == 'paper')):
        return negOne,three
    elif ((comp == 'rock') and (meat == 'scissors')) or ((meat == 'rock') and (comp == 'scissors')):
        return three,negOne
    elif ((comp == 'paper') and (meat == 'scissors')) or ((meat == 'paper') and (comp == 'scissors')):
        return negOne,three

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
