def isFactor(f,n):
    rmdr = n % f
    TV = (rmdr == 0)
    return TV

def factorsOf(n):
    Factors = []
    for i in range (1,n+1):
        if isFactor(i,n):
            Factors.append(i)
    return Factors

def isPrime(n):
    TV = len(factorsOf(n)) == 2
    return TV

def TableOfPrimes(From,To,nPerLine):
    for i in range(From,To):
        for i in range(nPerLine):
            if isPrime(To) == True:
                print(isPrime(To), end = '')

TableOfPrimes(1,20,6)


cntr = 0
for n in range(From,To+1):
    if isPrime(n):
        print(n, end = '')
        cntr += 1
        if isFactor(nPerLine,cntr):
            print()
