from math import sqrt,ceil

def isFactor(n,f):
    TV = n % f == 0
    return TV

def nextPrime(n):
    counter = 0
    for i in range(2,n - 1):
        if n % i == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False
        
    
def isPrime(n):
    for i in range (2,n):
        if nextPrime(i) == True:
            if isFactor(n,i) == True:
                return i
            

def allPrimeFactors(n):
    i = 0
    while n > 2:
        print (n,i)
        i = isPrime(n)
        n /= i
        print(n,i)
    

allPrimeFactors(20)
