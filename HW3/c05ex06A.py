# c05ex06A.py
#     Numerology of a multiple name - uses functions

def letter2Num(letter):
    '''
Computes number from letter.
'''
    n1 = ord(letter)
    n2 = n1 - ord('a') + 1
    return n2

def word2Num(word):
    '''
Computes number from word
'''
    accum = 0
    for letter in word:
        accum += letter2Num(letter)
    return accum    

def main():
    '''
Computes number of
a full name.
'''
    print("This program computes the 'number value' of a full name.")
    print()

    Names = input('Enter you full name: ')
    wordList = Names.split()

    accum = 0
    for word in wordList:
        accum += word2Num(word)
    
    print("The value is:", accum)

main()

#This program computes the 'number value' of a full name.
#
#Enter you full name: albert einstein
#The value is: 153
#>>> 