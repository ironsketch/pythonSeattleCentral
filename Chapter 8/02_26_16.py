def isPrime(n):
    test = 0
    for i in range(2,n - 1):
        if int(n / i) != 0:
            test += 1
    if test == 0:
        return True
    else:
        return False

def isFactor(f,n):
    if int(n / f) != 0:
        return True
    else:
        return False

def primeFactorsOf(n):
    for i in range(2,n):
        if isPrime(i) and isFactor(i,n):
            print(i,'is a prime number and a factor of',n)

##primeFactorsOf(9)
print(isPrime(3))
