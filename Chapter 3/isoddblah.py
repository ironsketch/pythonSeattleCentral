L = [1,2,3,4,5,6,7]

def isEven(sent):
    return sent % 2 == 0

def IDasEvenOrOdd(L):
    for n in L:
        if (isEven(n)):
            print (n, 'even')
        else:
            print (n, 'odd')

IDasEvenOrOdd(L)
