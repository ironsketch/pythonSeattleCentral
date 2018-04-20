# Variables

skipbonum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]

user1deck = []

user2deck = []

user1hand = []

user2hand = []

decksize = 0

prompt = ">>"

print ("Welcome to the game of Skipbo")
play = input("Ready to play? (yes or no)")

def main():
    if play == "yes":

        print ("You chose to play!")
        decksize = eval(input("Deck Size?"))

        pullcards (decksize, user1deck)
        pullcards (decksize, user2deck)

        print ("User 1: ", end=" ")
        print (user1deck[0])
        print ("User 2: ", end=" ")
        print (user2deck[0])

        startofplay (user1deck[0],user2deck[0])
    

    if play == "no":
        print ("You chose not to play!")

def pullcards (amount, userdeck):
    i = 0
    while i < amount:
        allcardsize = len(skipbonum) - 1
        from random import randint
        randomnum = randint(0, allcardsize)
        pullout = skipbonum[randomnum]
        varr = int(randomnum)
        skipbonum.pop(varr)
        userdeck.insert(0, pullout)
        i = i + 1

def startofplay (a,b):
    if a & b == "w":
        hand (1)
    elif a ^ b == "w":
        hand (2)
    elif a <= b:
        hand (3)
    else:
        hand (4)
        

def hand (number):
    print ("hand", number)
    

main ()
