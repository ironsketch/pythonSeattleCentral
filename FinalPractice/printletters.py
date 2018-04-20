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

def Loops(word1,word2):
    if len(word1) > len(word2):
        num = 0
        num2 = 2
        for i in range(len(word1) - 1):
            print(word1[num:num2] + word2[num:num2])
            num += 1
            num2 += 1
    else:
        num = 0
        num2 = 2
        for i in range(len(word2) - 1):
            print(word1[num:num2] + word2[num:num2])
            num += 1
            num2 += 1

Loops('top','guns')
##print(eveWholeNum())
##printLetters('Shit')
##print(sumDigits(1234))
