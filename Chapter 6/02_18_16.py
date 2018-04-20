def CT(pH):
    ranVal = random()
    if ranVal <= pH:
        return 1
    else:
        return 0

def factorial(n):
    prodAcum = 1
    for i in range(n,1,-1):
        prodAcum *= i
    return prodAcum

def C(nTosses,nHeads):
    num = factorial(nTosses)
    denom = factorial(nHeads) * factorial(nTosses - nHeads)
    val = num/denom
    return val

def predProb(nTosses,nHeads,pH):
    nTails = nTosses - nHeads
    pT = 1 - pH
    Pr = C(nTosses,nHeads) * (pH**nHeads) * (pT**nTails)
    return pT

for nHeads in range (0,6):
    print (nHeads,predProb(5,nHeads,.5))
