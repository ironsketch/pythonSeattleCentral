from math import sqrt,ceil

def isFactor(n,f):
    '''
Returns True if f is a factor of n.
OTW returns False.  n is an int.
'''
    TV = n % f == 0
    return TV

def properFactorsOf(n):
    '''
Returns a list of all proper factors f of n
where 2 <= f <= n/2.
'''
    factors = []
    for x in range(2,n//2+1):
        if isFactor(n,x):
            factors.append(x)
    return factors

def isPrime(n):
    '''
Returns True if n is prime,
OTW returns False.  n is an int.
'''
    for f in range(2,int(sqrt(n))+1):
        #print(f,isFactor(n,f))
        if isFactor(n,f):
            return False
##    TV = len(properFactorsOf(n)) == 0
    return True

def multOfFactor(n,f):
    '''
Returns the multiplicity of f, that is
highest exponent of f that divides n.
'''
    count = 0
    while isFactor(n,f):
        count += 1
        n /= f
    return count

def primeFactorsOf(n):
    '''
Returns a list of the prime factors of n.
'''
    PF = {}
    if isPrime(n):
        return [n]
    else:
        f = 2
        while f <= n:
            m = multOfFactor(n,f)
            if m > 0:
                PF[f] = m
                n  /= f**m
            f += 1           
    return PF       
        
print(primeFactorsOf(1234567890123456789))

##for n in range(2,20):
##    print(n,isPrime(n))

