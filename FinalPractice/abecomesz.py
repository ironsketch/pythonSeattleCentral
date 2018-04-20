

def encodeLtr(x):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    indx = alpha.index(x)
    indx = (indx - 25) * -1
    letter = alpha[indx]
    
    return letter

def encodeWord(w):
    w = w.lower()
    newWord = ''
    for letter in w:
        l = encodeLtr(letter)
        newWord += l

    return newWord

def encodePhrase(p):
    p = p.split()
    newPhrase = ''
    for word in p:
        nWord = encodeWord(word)
        newPhrase += nWord + ' '
        
    return newPhrase

def encodeAndReverseWords(Phrase):
    backwords = ''
    Phrase = encodePhrase(Phrase)
    Phrase = Phrase.split()
    for word in Phrase:
        backwords = word + ' ' + backwords

    return backwords

print(encodeAndReverseWords('Poopy Shit'))

