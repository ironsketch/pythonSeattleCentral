# c05ex05A.py
#     Numerology of a single name - uses functions

def letter2Num(letter):
    '''
Computes number from letter.
'''
    n1 = ord(letter)
    letterVal = n1 - ord('a') + 1
    return letterVal

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
get user single name
set sum accumulator to zero
make all letter lower case
for each letter in name
    take ord of letter
    subtract ord(a) and add 1 (a ~ 1, b ~ 2, etc)
    add to sum accumulator
print out resulting sum
'''
    print("This program computes the 'number value' of a single name")
    print()
    name = input('Enter a name: ')
    print("The number value of '{0}' is {1}.".format(name,word2Num(name)))

main()

#>>> for letter in 'abcdqrswxyz':
#...         print(letter,letter2Num(letter))
#... 
#a 1
#b 2
#c 3
#d 4
#q 17
#r 18
#s 19
#w 23
#x 24
#y 25
#z 26
#>>> word2Num('abcd')
#10
#>>> main()
#This program computes the 'number value' of a name
#
#Enter a name: abcd efgh
#The number value of 'abcd efgh' is -28. # Note that this does not work.  Why?
#>>> main()
#This program computes the 'number value' of a name
#
#Enter a name: zelle
#The number value of 'zelle' is 60.
#>>> 