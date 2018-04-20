def isFactor(i,n):
    if n % i == 0:
        return i

def factorsOf(n):
    Factors = []
    for i in range (1,n+1):
        Factors.append(isFactor(i,n))
    return Factors


print(factorsOf(12))


