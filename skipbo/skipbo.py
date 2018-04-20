
# Variables

skipboNum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]

user1Deck = []

user2Deck = []

user1Hand = []

user2Hand = []

deckSize = 0

handCount = 5


# Design
def createWindow():
    win = GraphWin("SkipBo", 400, 300)




print ("Welcome to the game of Skipbo")
play = input("Ready to play? (yes or no) ")

def main():
    if play == "yes":

        print ("You chose to play!")
        deckSize = eval(input("Deck Size? "))

        pullCards (deckSize, user1Deck)
        pullCards (deckSize, user2Deck)

        print ("User 1: ", end=" ")
        print (user1Deck[0])
        print ("User 2: ", end=" ")
        print (user2Deck[0])

        startOfPlay (user1Deck[0],user2Deck[0])

        print (len(user1Hand))

        displayHand ()

    if play == "no":
        print ("You chose not to play!")

def pullCards (amount, userDeck):
    i = 0
    while i < amount:
        allCardSize = len(skipboNum) - 1
        from random import randint
        randomNum = randint(0, allCardSize)
        pullOut = skipboNum[randomNum]
        varr = int(randomNum)
        skipboNum.pop(varr)
        userDeck.insert(0, pullOut)
        i = i + 1

def startOfPlay (a,b):
    if (a == "w" and b == "w"):
        pullCards (handCount, user1Hand)
    elif (a != "w" and b == "w"):
        pullCards (handCount, user2Hand)
    elif (a == "w" and b != "w"):
        pullCards (handCount, user1Hand)
    elif a < b:
        pullCards (handCount, user1Hand)
    else:
        pullCards (handCount, user2Hand)

def displayHand ():
    print ("Your hand: ", end=' ')
    for i in user1Hand:
        print (i, end=' ')
    print (' ')
    

main ()
