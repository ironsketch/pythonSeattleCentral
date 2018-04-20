def nthLtr_nTimes(word):
    L = []
    counter = 1
    for letter in word:
        L.append(letter*counter)
        counter += 1
    return L

def putSpaceBtwnLtrds(Strg):
    Split = []
    Joined = ''
    for letter in Strg:
        Split.append(letter)

    counter = 0
    for i in range (len(Split) - 1):
        Joined += Split[counter] + ' '
        counter += 1
    Joined += Split[len(Split) - 1]
    return Joined

def pyramidFrom(Word):
    L = nthLtr_nTimes(Word)
    for item in L:
        print('{:^30}'.format(putSpaceBtwnLtrds(item)))

def countPyramidChars(Word):
    L = nthLtr_nTimes(Word)
    Accum = 0
    for item in L:
        Accum += len(putSpaceBtwnLtrds(item))
    return Accum

def pyramidFromNoRepeatLtrs(Word):
    a = ''
    for letter in Word:
        if letter not in a:
            a += letter
    pyramidFrom(a)
    
pyramidFromNoRepeatLtrs('mississippi')
