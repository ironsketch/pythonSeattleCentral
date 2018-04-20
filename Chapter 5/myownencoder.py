key = "q*&^%$#@!)poiuytre?k:><}{|"
key2 = ")(*$%^&#@!owjfudbns<>?z:{}"
alpha = "abcdefghijklmnopqrstuvwxyz"

def encode(text):
    cipher=''

    apart = text.split()
    for word in text:
        for letter in word:
            index = alpha.find(letter)
            
            if index >= 0:
                cipher += key[index2]
                index2 = key.find(cipher)
                
            else:
                cipher += ' '
    return cipher

def decode(text):
    cipher=''

    apart = text.split()
    for word in text:
        for letter in word:
            index2 = key2.find(letter)
            index = key.find(index2)
            if index >= 0:
                cipher += alpha[index]
            else:
                cipher += ' '
    return cipher

def main():
    print('Caesar cipher\n')
    text = input('Enter something to decode:')
    text = text.lower()

    print('Your secret code:')
    reprocess = encode(text)
    print(reprocess)
    print('++++++++++++++++++')
    print('Your original message:')
    print(decode(reprocess))

    

main()
