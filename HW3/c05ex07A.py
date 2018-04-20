# c05ex07A.py
#    Caesar cipher (non-circular), uses function

def shiftLetter(letter,key):
    '''
Applies Caesar cipher to letter using key.
'''
    L1 = ord(letter)
    L2 = ord(letter) + key
    A = chr(L2)
    return A

def shiftWord(word,key):
    '''
Applies Caesar ciper to word using key.
'''
    accum = ''
    for letter in word:
        accum += shiftLetter(letter,key)
    return accum

def encodeMsg(msg,key):
    '''
Applies Caesar cipher to a multiword
msg, returns encoded msg.
'''
    cipher = ""
    wordList = msg.split()
    for word in wordList:
        cipher += shiftWord(word,key)
        cipher += ' '
    cipher1 = cipher[:-1]     ## take off leading space
    return cipher1
    
    
def main():
    '''
Gets msg from user, returns
msg encoded w Caesar cipher.
'''
    print("Caesar cipher")
    print()

    key = eval(input("Enter the key value: "))
    plain = input("Enter the phrase to encode: ")
    
    
    print("Encoded message follows:")
    print(encodeMsg(plain,key))

main()

#Caesar cipher
#
#Enter the key value: 2
#Enter the phrase to encode: pigs are great!
#Encoded message follows:
#rkiu ctg itgcv#
#>>> 