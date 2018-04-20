def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def isPrime(n):
    TV = len(prime_factors(n)) == 1
    return TV

def isSmithNumber(n):
    TV1 = not isPrime(n)
    TV2 = digitSum(n) == digitSumOf(prime_factors(n))
    return TV1 and TV2

def digitSum(n):
    SumDig = 0
    for dig in str(n):
        SumDig += int(dig)
    return SumDig

def digitSumOf(L):
    sumAcum = 0
    for num in L:
        sumAcum += digitSum(num)
    return sumAcum

def printToFile():
    fileOpen = open('numbers.txt', 'w')
    counter = 1
    for i in range (2,1000000):
        if isSmithNumber(i) == True:
            if counter % 20 != 0:
                print('{:<8}'.format(i),end='',file = fileOpen)
            else:
                print('{:<8}'.format(i),file = fileOpen)
            counter += 1
            
                
    fileOpen.close()

printToFile()
