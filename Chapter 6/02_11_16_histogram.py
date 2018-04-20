alphaDict = {}

word = 'mother fucker arf'

def histogram(word):
    for letter in word:
        if letter in alphaDict:
            alphaDict[letter] += 1
            
        else:
            alphaDict[letter] = 1
            
histogram(word)
print(alphaDict)
