def printLetters(word):
    length = len(word)
    for letter in word:
        print('{}'.format(letter*length))
        length -= 1

def sumDigits(n):
    number = str(n)
    total = 0
    for num in number:
        total += int(num)
    return total

def sumDigitsIs(Sum,From,To):
    nums = []
    for i in range (From,To + 1):
        if sumDigits(i) == Sum:
            nums.append(i)
    return nums

def eveWholeNum():
    a = sumDigitsIs(13,100000,200000)
    b = sumDigitsIs(14,100000,200000)
    L = a + b
    c = []
    for num in L:
        if num % 2 == 0:
            c.append(num)
    return len(c)


def wordLoop(word,many):
    num = 0
    num2 = many
    L = []
    for i in range(len(word) - (many - 1)):
        L.append(word[num:num2])
        num += 1
        num2 += 1
    return L

def Loops(word1,word2,num):
    L = []
    wordOne = wordLoop(word1,num)
    wordTwo = wordLoop(word2,num)
    if len(wordOne) < len(wordTwo):
        for word in wordOne:
            L.append(word)
        for i in range (len(L)):
            L[i] += wordTwo[i]
    else:
        for word in wordTwo:
            L.append(word)
        for i in range (len(L)):
            L[i] += wordOne[i]
    print(L)

Loops('top','guns',2)
##print(eveWholeNum())
##printLetters('Shit')
##print(sumDigits(1234))
