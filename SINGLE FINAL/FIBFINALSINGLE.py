def NewFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        a,b,c = 0,1,2
        for i in range (n - 3):
            a,b,c = b,c,a + b + c
        return c

def TermsOfNewFib(n):
    L = []
    for i in range (1,n + 1):
        L.append(NewFib(i))
    return L

def SumOfNewFibTerms(n):
    L = TermsOfNewFib(n)
    Accum = 0
    for num in L:
        Accum += num
    return Accum

def NumOfNewFibTermsToGet(Sum):
    check = 1
    while SumOfNewFibTerms(check) < Sum:
        check += 1
    return len(TermsOfNewFib(check))

def rankInts(n):
    rankDict = {}
    for i in range (1,n + 1):
        rankDict[i] = round(i / NumOfNewFibTermsToGet(i),1)
    return rankDict

def main():
    DictSim = {} # Simplified Dict with only counter for each rank
    RankDict = rankInts(500)
    for item in RankDict: # Appending each similar rank to new Dict and adding Accum
        a = RankDict[item]
        if a in DictSim:
            DictSim[a] += 1
        else:
            DictSim[a] = 1
    print('{:>20} {:>20}'.format('Rank','Num of Times'))
    Accum = 0
    for rank in DictSim:
        if DictSim[rank] > 1:
            print('{:>20} {:>20}'.format(rank,DictSim[rank]))
            Accum += 1
    print('There are,',Accum,'number of ranks having 2 or more ints that share that rank')

main()
